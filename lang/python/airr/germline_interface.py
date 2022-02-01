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

if (sys.version_info > (3, 0)):
    from io import StringIO
else: # Python 2 code in this block
    from io import BytesIO as StringIO




# Load imports
from airr.schema import ValidationError, GermlineSetSchema

def load_object(filename, object_name, schema, validate=False, debug=False):
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

    if object_name not in md:
        if debug:
            sys.stderr.write('%s is missing "Repertoire" key\n' % (filename))
        raise KeyError('Repertoire object cannot be found in the file')

    # validate if requested
    if validate:
        validate_object(md[object], object_name, schema, debug)

    # we do not perform any additional processing
    return md


def write_object(filename, md, debug=False):
    # determine file type from extension and use appropriate loader
    ext = filename.split('.')[-1]
    if ext == 'yaml' or ext == 'yml':
        with open(filename, 'w') as handle:
            for instance in md:
                yaml.dump(instance, handle, default_flow_style=False)
    elif ext == 'json':
        with open(filename, 'w') as handle:
            json.dump(md, handle, sort_keys=False, indent=2)
    else:
        if debug:
            sys.stderr.write('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % (ext))
        raise TypeError('Unknown file type: %s. Supported file extensions are "yaml", "yml" or "json"\n' % (ext))

    return True


def validate_object(object, object_name, object_schema, debug=False):
    valid = True
    try:
        object_schema.validate_object(object)
    except ValidationError as e:
        valid = False
        if debug:
            sys.stderr.write('%s has validation error: %s\n' % (object_name, e))
    if not valid:
        raise ValidationError('%s has validation errors\n' % (object_name))


def load_germline_set(filename, validate=False, debug=False):
    """
    Read an AIRR germline set file into a GermlineSet

    Arguments:
      file (str): path to the input file.
      validate (bool): whether to validate data as it is read, raising a ValidationError
                       exception in the event of an error.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      airr.germline_set.GermlineSet - germline set object
    """

    return load_object(filename, 'GermlineSet', GermlineSetSchema, validate=validate, debug=debug)


def write_germline_set(filename, germline_set, debug=False):
    """
    Write a GermlineSet to a file

    Arguments:
      filename (str): output file path.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      None
    """

    md = OrderedDict()
    md['GermlineSet'] = germline_set
    write_object(filename, md, debug)


def validate_germline_set(germline_set, debug=False):
    """
    Validates an AIRR rearrangements object

    Arguments:
      germline_set (GermlineSet): the object to validate
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files passed validation, otherwise False.
    """

    return validate_object(germline_set, GermlineSetSchema, debug=debug)


def validate_germline_set_file(filename, debug=False):
    """
    Validates an AIRR rearrangements object

    Arguments:
      germline_set (GermlineSet): the object to validate
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files passed validation, otherwise False.
    """

    load_germline_set(filename, validate=True, debug=debug)

