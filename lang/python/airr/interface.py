"""
Interface functions for file operations
"""
from __future__ import absolute_import

# System imports
import sys
import pandas as pd
from collections import OrderedDict
from itertools import chain
from pkg_resources import resource_filename
import json
import yaml
import yamlordereddictloader
from io import open

# Load imports
from airr.io import RearrangementReader, RearrangementWriter
from airr.schema import ValidationError, RearrangementSchema, RepertoireSchema


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

    return RearrangementReader(open(filename, 'r'), validate=validate, debug=debug)


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
    # schema = RearrangementSchema
    # df = pd.read_csv(handle, sep='\t', header=0, index_col=None,
    #                  dtype=schema.numpy_types(), true_values=schema.true_values,
    #                  false_values=schema.true_values)
    # return df
    with open(filename, 'r') as handle:
        reader = RearrangementReader(handle, validate=validate, debug=debug)
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
        readers = [RearrangementReader(open(f, 'r'), debug=debug) for f in in_filenames]
        field_list = [x.fields for x in readers]
        if drop:
            field_set = set.intersection(*map(set, field_list))
        else:
            field_set = set.union(*map(set, field_list))
        field_order = OrderedDict([(f, None) for f in chain(*field_list)])
        out_fields = [f for f in field_order if f in field_set]

        # write input files to output file sequentially
        with open(out_filename, 'w+') as handle:
            writer = RearrangementWriter(handle, fields=out_fields, debug=debug)
            for reader in readers:
                for r in reader:  writer.write(r)
                reader.close()
    except:
        sys.stderr.write('Error occurred while merging AIRR rearrangement files.\n')
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


def load_repertoire(filename, validate=False, debug=False):
    """
    Load an AIRR repertoire metadata file

    Arguments:
      filename (str): path to the input file.
      validate (bool): whether to validate data as it is read, raising a ValidationError
                       exception in the event of an error.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      list: list of Repertoire dictionaries.
    """
    # Because the repertoires are read in completely, we do not bother
    # with a reader class.
    md = None

    # determine file type from extension and use appropriate loader
    ext = filename.split('.')[-1]
    if ext in ('yaml', 'yml'):
        with open(filename, 'r', encoding='utf-8') as handle:
            md = yaml.load(handle, Loader=yamlordereddictloader.Loader)
    elif ext == 'json':
        with open(filename, 'r', encoding='utf-8') as handle:
            md = json.load(handle)
    else:
        if debug:
            sys.stderr.write('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % (ext))
        raise TypeError('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % (ext))

    if md.get('Repertoire') is None:
        if debug:
            sys.stderr.write('%s is missing "Repertoire" key\n' % (filename))
        raise KeyError('Repertoire object cannot be found in the file')

    # validate if requested
    if validate:
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

    # determine file type from extension and use appropriate loader
    ext = filename.split('.')[-1]
    if ext == 'yaml' or ext == 'yml':
        with open(filename, 'w') as handle:
            md = yaml.dump(md, handle, default_flow_style=False)
    elif ext == 'json':
        with open(filename, 'w') as handle:
            md = json.dump(md, handle, sort_keys=False, indent=2)
    else:
        if debug:
            sys.stderr.write('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % (ext))
        raise TypeError('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % (ext))
        
    return True


def repertoire_template():
    """
    Return a blank repertoire object from the template. This object has the complete
    structure with all of the fields and all values set to None or empty string.

    Returns:
      object: empty repertoire object.
    """
    
    # TODO: I suppose we should dynamically create this from the schema
    # versus loading a template.

    # Load blank template
    f = resource_filename(__name__, 'specs/blank.airr.yaml')
    object = load_repertoire(f)

    return object['Repertoire'][0]

