"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""
from airr.io import RearrangementReader, RearrangementWriter
from collections import OrderedDict
from itertools import chain


def read(handle, debug=False):
    """
    Open an AIRR rearrangements file and read its contents

    Arguments:
      handle (file): input file handle.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      airr.io.RearrangementReader: open reader class.
    """
    return RearrangementReader(handle, debug=debug)


def create(handle, fields=None, debug=False):
    """
    Create an empty AIRR rearrangements file

    Arguments:
      handle (file): output file handle.
      fields (list): additional non-required fields to add to the output.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      airr.io.RearrangementWriter: open writer class.
    """
    return RearrangementWriter(handle, fields=fields, debug=debug)


def derive(out_handle, in_handle, fields=None, debug=False):
    """
    Create an empty AIRR rearrangements file with fields derived from an existing file

    Arguments:
      out_handle (file): output file handle.
      in_handle (file): existing file to derive fields from
      fields (list): additional non-required fields to add to the output.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      airr.io.RearrangementWriter: open writer class.
    """
    reader = RearrangementReader(in_handle)
    in_fields = list(reader.fields)
    if fields is not None:
        in_fields.extend([f for f in fields if f not in in_fields])
    return RearrangementWriter(out_handle, fields=in_fields, debug=debug)

def merge(out_handle, airr_files, drop=False, debug=False):
    """
    Merge one or more AIRR rearrangements files

    Arguments:
      out_handle (file): output file handle.
      airr_files (list): list of input files to merge.
      drop (bool): drop flag. If True then drop fields that do not exist in all input
                   files, otherwise combine fields from all input files.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      boolean: True if files were successfully merged, otherwise False.
    """
    try:
        # gather fields from input files
        readers = [RearrangementReader(open(f, 'r'), debug=debug) for f in airr_files]
        field_list = [x.fields for x in readers]
        if drop:
            field_set = set.intersection(*map(set, field_list))
        else:
            field_set = set.union(*map(set, field_list))
        field_order = OrderedDict([(f, None) for f in chain(*field_list)])
        out_fields = [f for f in field_order if f in field_set]

        out_file = RearrangementWriter(out_handle, fields=out_fields, debug=debug)

        for reader in readers:
            for rec in reader:
                out_file.write(rec)

        out_file.close()
        return True
    except:
        return False

def validate(airr_files, debug=False):
    """
    Validates one or more AIRR rearrangements files

    Arguments:
      in_files (list): list of input files to validate.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      boolean: True if all files passed validation, otherwise False
    """
    valid = True
    for file in airr_files:
        reader = RearrangementReader(open(file, 'r'))
        valid &= reader.validate()
        # TODO: how to close file?

    return valid

# versioneer-generated
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
