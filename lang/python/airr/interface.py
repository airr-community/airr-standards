"""
Interface functions for file operations
"""
from __future__ import absolute_import

# System imports
import gzip
import json
import os
import sys
import pandas as pd
import yaml
import yamlordereddictloader
from collections import OrderedDict
from itertools import chain
from io import open
from pkg_resources import resource_filename
from warnings import warn

if (sys.version_info > (3, 0)):
    from io import StringIO
else:
    # Python 2 code in this block
    from io import BytesIO as StringIO

# Load imports
from airr.io import RearrangementReader, RearrangementWriter
from airr.schema import Schema, RearrangementSchema, RepertoireSchema, AIRRSchema, DataFileSchema, ValidationError

#### Rearrangement ####

def read_rearrangement(filename, validate=False, debug=False):
    """
    Open an iterator to read an AIRR rearrangements file

    Arguments:
      file (str): path to the input file.
      validate (bool): whether to validate data as it is read, raising a ValidationError
                       exception in the event of an error.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      airr.io.RearrangementReader: iterable reader class.
    """
    if filename.endswith(".gz"):
        handle = gzip.open(filename, 'r')
    else:
        handle = open(filename, 'r')
        
    return RearrangementReader(handle, validate=validate, debug=debug)


def create_rearrangement(filename, fields=None, debug=False):
    """
    Create an empty AIRR rearrangements file writer

    Arguments:
      filename (str): output file path.
      fields (list): additional non-required fields to add to the output.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      airr.io.RearrangementWriter: open writer class.
    """
    return RearrangementWriter(open(filename, 'w+'), fields=fields, debug=debug)


def derive_rearrangement(out_filename, in_filename, fields=None, debug=False):
    """
    Create an empty AIRR rearrangements file with fields derived from an existing file

    Arguments:
      out_filename (str): output file path.
      in_filename (str): existing file to derive fields from.
      fields (list): additional non-required fields to add to the output.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      airr.io.RearrangementWriter: open writer class.
    """
    reader = RearrangementReader(open(in_filename, 'r'))
    in_fields = list(reader.fields)
    if fields is not None:
        in_fields.extend([f for f in fields if f not in in_fields])

    return RearrangementWriter(open(out_filename, 'w+'), fields=in_fields, debug=debug)


def load_rearrangement(filename, validate=False, debug=False):
    """
    Load the contents of an AIRR rearrangements file into a data frame

    Arguments:
      filename (str): input file path.
      validate (bool): whether to validate data as it is read, raising a ValidationError
                       exception in the event of an error.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      pandas.DataFrame: Rearrangement records as rows of a data frame.
    """
    # TODO: test pandas.DataFrame.read_csv with converters argument as an alterative
    schema = RearrangementSchema

    df = pd.read_csv(filename, sep='\t', header=0, index_col=None,
                     dtype=schema.pandas_types(), true_values=schema.true_values,
                     false_values=schema.false_values)
    # added to use RearrangementReader without modifying it:
    buffer = StringIO()  # create an empty buffer
    df.to_csv(buffer, sep='\t', index=False)  # fill buffer
    buffer.seek(0)  # set to the start of the stream

    reader = RearrangementReader(buffer, validate=validate, debug=debug)

    df = pd.DataFrame(list(reader))
    return df


def dump_rearrangement(dataframe, filename, debug=False):
    """
    Write the contents of a data frame to an AIRR rearrangements file

    Arguments:
      dataframe (pandas.DataFrame): data frame of rearrangement data.
      filename (str): output file path.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if the file is written without error.
    """
    # TODO: test pandas.DataFrame.to_csv with converters argument as an alterative
    # dataframe.to_csv(handle, sep='\t', header=True, index=False, encoding='utf-8')

    fields = dataframe.columns.tolist()
    with open(filename, 'w+') as handle:
        writer = RearrangementWriter(handle, fields=fields, debug=debug)
        for __, row in dataframe.iterrows():
            writer.write(row.to_dict())

    return True


def merge_rearrangement(out_filename, in_filenames, drop=False, debug=False):
    """
    Merge one or more AIRR rearrangements files

    Arguments:
      out_filename (str): output file path.
      in_filenames (list): list of input files to merge.
      drop (bool): drop flag. If True then drop fields that do not exist in all input
                   files, otherwise combine fields from all input files.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files were successfully merged, otherwise False.
    """
    try:
        # gather fields from input files
        readers = (RearrangementReader(open(f, 'r'), debug=False) for f in in_filenames)
        field_list = [x.fields for x in readers]
        if drop:
            field_set = set.intersection(*map(set, field_list))
        else:
            field_set = set.union(*map(set, field_list))
        field_order = OrderedDict([(f, None) for f in chain(*field_list)])
        out_fields = [f for f in field_order if f in field_set]

        # write input files to output file sequentially
        readers = (RearrangementReader(open(f, 'r'), debug=debug) for f in in_filenames)
        with open(out_filename, 'w+') as handle:
            writer = RearrangementWriter(handle, fields=out_fields, debug=debug)
            for reader in readers:
                for r in reader:  writer.write(r)
                reader.close()
    except Exception as e:
        sys.stderr.write('Error occurred while merging AIRR rearrangement files: %s\n' % e)
        return False

    return True


def validate_rearrangement(filename, debug=False):
    """
    Validates an AIRR rearrangements file

    Arguments:
      filename (str): path of the file to validate.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files passed validation, otherwise False.
    """
    valid = True
    if debug:
        sys.stderr.write('Validating: %s\n' % filename)

    # Open reader
    handle = open(filename, 'r')
    reader = RearrangementReader(handle, validate=True)

    # Validate header
    try:
        iter(reader)
    except ValidationError as e:
        valid = False
        if debug:
            sys.stderr.write('%s has validation error: %s\n' % (filename, e))

    # Validate each row
    i = 0
    while True:
        try:
            i = i + 1
            next(reader)
        except StopIteration:
            break
        except ValidationError as e:
            valid = False
            if debug:
                sys.stderr.write('%s at record %i has validation error: %s\n' % (filename, i, e))

    # Close
    handle.close()

    return valid

#### AIRR Data Model ####

def read_airr(filename, format=None, validate=False, adf=True, debug=False):
    """
    Load an AIRR Data file

    Arguments:
      filename (str): path to the input file.
      format (str): input file format valid strings are "yaml" or "json". If set to None,
                    the file format will be automatically detected from the file extension.
      validate (bool): whether to validate data as it is read, raising a ValidationError
                       exception in the event of a validation failure.
      adf (bool): If True only validate objects defined in the AIRR DataFile schema.
                  If False, attempt validation of all top-level objects.
                  Ignored if validate=False.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      dict: dictionary of AIRR Data objects.
    """
    # Because the AIRR Data File is read in completely, we do not bother with a reader class.
    # Determine file type from extension and use appropriate loader
    ext = str.lower(filename.split('.')[-1]) if not format else format
    if ext in ('yaml', 'yml'):
        with open(filename, 'r', encoding='utf-8') as handle:
            data = yaml.load(handle, Loader=yamlordereddictloader.Loader)
    elif ext == 'json':
        with open(filename, 'r', encoding='utf-8') as handle:
            data = json.load(handle)
    else:
        if debug:  sys.stderr.write('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % ext)
        raise TypeError('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % ext)
        data = None

    # Validate if requested
    if validate:
        if debug:  sys.stderr.write('Validating: %s\n' % filename)
        try:
            valid = validate_airr(data, adf=adf, debug=debug)
        except ValidationError as e:
            if debug:  sys.stderr.write('%s failed validation\n' % filename)
            raise ValidationError(e)

    # We do not perform any additional processing
    return data


def validate_airr(data, adf=True, debug=False):
    """
    Validates an AIRR Data file

    Arguments:
      data (dict): dictionary containing AIRR Data Model objects
      adf (bool): If True only validate objects defined in the AIRR DataFile schema.
                  If False, attempt validation of all top-level objects
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files passed validation, otherwise False.
    """
    # Type check that input type is either dict or OrderedDict
    if not hasattr(data, 'items'):
        if debug:  sys.stderr.write('Data parameter is not a dictionary\n')
        raise TypeError('Data parameter is not a dictionary')

    # Loop through each AIRR object and validate
    valid = True
    for k, object in data.items():
        if k in ('Info', 'DataFile'):  continue
        if not object:  continue

        # Check for DataFile schema
        if adf and k not in DataFileSchema.properties:
            if debug:  sys.stderr.write('Skipping non-DataFile object: %s\n' % k)
            continue

        # Get Schema
        schema = AIRRSchema.get(k, Schema(k))

        # Determine input type and set appropriate iterator
        if hasattr(object, 'items'):
            # Validate named array (dict)
            obj_iter = object.items()
            # Validate named array (dict) or a single object (dict)
            # obj_iter = object.items() if 'definition' not in object.keys() else [0, object]
        elif isinstance(object, list):
            # Validate array
            obj_iter = enumerate(object)
        else:
            # Unrecognized data structure
            valid = False
            if debug:  sys.stderr.write('%s is an unrecognized data structure: %s\n' % k)
            continue

        # Validate each record in array
        for i, record in obj_iter:
            try:
                schema.validate_object(record)
            except ValidationError as e:
                valid = False
                if debug:  sys.stderr.write('%s at array position %s with validation error: %s\n' % (k, i, e))

    if not valid:
        raise ValidationError('AIRR Data Model has validation failures')

    return valid


def write_airr(filename, data, format=None, info=None, validate=False, adf=True, debug=False):
    """
    Write an AIRR Data file

    Arguments:
      filename (str): path to the output file.
      data (dict): dictionary of AIRR Data Model objects.
      format (str): output file format valid strings are "yaml" or "json". If set to None,
                    the file format will be automatically detected from the file extension.
      info (object): info object to write. Will write current AIRR Schema info if not specified.
      validate (bool): whether to validate data before it is written, raising a ValidationError
                       exception in the event of a validation failure.
      adf (bool): If True only validate and write objects defined in the AIRR DataFile schema.
                  If False, attempt validation and write of all top-level objects
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if the file is written without error.
    """
    # Type check that input type is either dict or OrderedDict
    if not hasattr(data, 'items'):
        if debug:  sys.stderr.write('Data parameter is not a dictionary\n')
        raise TypeError('Data parameter is not a dictionary')

    # Validate if requested
    if validate:
        if debug:  sys.stderr.write('Validating: %s\n' % filename)
        try:
            valid = validate_airr(data, adf=adf, debug=debug)
        except ValidationError as e:
            if debug:  sys.stderr.write(e)
            raise ValidationError(e)

    md = OrderedDict()
    if info is None:
        info = RearrangementSchema.info.copy()
        info['title'] = 'AIRR Data File'
        info['description'] = 'AIRR Data File written by AIRR Standards Python Library'
    md['Info'] = info

    # Loop through each object and add them to the output dict
    for k, obj in data.items():
        if k in ('Info', 'DataFile'):  continue
        if not obj:  continue
        if adf and k not in DataFileSchema.properties:
            if debug:  sys.stderr.write('Skipping non-DataFile object: %s\n' % k)
            continue
        md[k] = obj

    # Determine file type from extension and use appropriate loader
    ext = str.lower(filename.split('.')[-1]) if not format else format
    if ext in ('yaml', 'yml'):
        with open(filename, 'w') as handle:
            yaml.dump(md, handle, default_flow_style=False)
    elif ext == 'json':
        with open(filename, 'w') as handle:
            json.dump(md, handle, sort_keys=False, indent=2)
    else:
        if debug:
            sys.stderr.write('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % ext)
        raise TypeError('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % ext)

    return True


#### Deprecated ####

def repertoire_template():
    """
    Return a blank repertoire object from the template. This object has the complete
    structure with all of the fields and all values set to None or empty string.

    Returns:
      object: empty repertoire object.
    """
    # Deprecation
    warn('repertoire_template is deprecated and will be removed in a future release.\nUse RepertoireSchema.template() instead.\n',
         DeprecationWarning, stacklevel=2)

    # Build template
    object = RepertoireSchema.template()

    return object


def load_repertoire(filename, validate=False, debug=False):
    """
    Load an AIRR repertoire metadata file

    Arguments:
      filename (str): path to the input file.
      validate (bool): whether to validate data as it is read, raising a ValidationError
                       exception in the event of an error.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      dict: dictionary of AIRR Data objects.
    """
    # Deprecation
    warn('load_repertoire is deprecated and will be removed in a future release.\nUse read_airr instead.\n',
         DeprecationWarning, stacklevel=2)

   # use standard load function, we only validate Repertoire if requested
    md = read_airr(filename, validate=validate, debug=debug)

    if md.get('Repertoire') is None:
        if debug:
            sys.stderr.write('%s is missing "Repertoire" key\n' % (filename))
        raise KeyError('Repertoire object cannot be found in the file')

    # validate if requested
    if validate:
        valid = True
        reps = md['Repertoire']
        i = 0
        for r in reps:
            try:
                RepertoireSchema.validate_object(r)
            except ValidationError as e:
                valid = False
                if debug:
                    sys.stderr.write('%s has repertoire at array position %i with validation error: %s\n' % (filename, i, e))
            i = i + 1
        if not valid:
            raise ValidationError('Repertoire file %s has validation errors\n' % (filename))

    # we do not perform any additional processing
    return md


def validate_repertoire(filename, debug=False):
    """
    Validates an AIRR repertoire metadata file

    Arguments:
      filename (str): path of the file to validate.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files passed validation, otherwise False.
    """
    # Deprecation
    warn('validate_repertoire is deprecated and will be removed in a future release.\nUse validate_airr instead.\n',
         DeprecationWarning, stacklevel=2)

    valid = True
    if debug:
        sys.stderr.write('Validating: %s\n' % filename)

    # load with validate
    try:
        data = load_repertoire(filename, validate=True, debug=debug)
    except TypeError:
        valid = False
    except KeyError:
        valid = False
    except ValidationError as e:
        valid = False
        if debug:
            sys.stderr.write('%s has validation error: %s\n' % (filename, e))

    return valid

def write_repertoire(filename, repertoires, info=None, debug=False):
    """
    Write an AIRR repertoire metadata file

    Arguments:
      file (str): path to the output file.
      repertoires (list): array of repertoire objects.
      info (object): info object to write. Will write current AIRR Schema info if not specified.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if the file is written without error.
    """
    # Deprecation
    warn('write_repertoire is deprecated and will be removed in a future release.\nUse write_airr instead.\n',
         DeprecationWarning, stacklevel=2)

    if not isinstance(repertoires, list):
        if debug:
            sys.stderr.write('Repertoires parameter is not a list\n')
        raise TypeError('Repertoires parameter is not a list')

    md = OrderedDict()
    if info is None:
        info = RearrangementSchema.info.copy()
        info['title'] = 'Repertoire metadata'
        info['description'] = 'Repertoire metadata written by AIRR Standards Python Library'
    md['Info'] = info
    md['Repertoire'] = repertoires

    return write_airr(filename, md, info=info, debug=debug)
