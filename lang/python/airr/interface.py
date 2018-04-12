"""
Interface functions for file operations
"""
# System imports
import pandas as pd
import os
from collections import OrderedDict
from itertools import chain

# Load imports
from airr.io import RearrangementReader, RearrangementWriter


def read(handle, debug=False):
    """
    Open an iterator to read an AIRR rearrangements file

    Arguments:
      handle (file): input file handle.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      airr.io.RearrangementReader: iterable reader class.
    """
    return RearrangementReader(handle, debug=debug)


def create(handle, fields=None, debug=False):
    """
    Create an empty AIRR rearrangements file writer

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


def load(handle, debug=False):
    """
    Load the contents of an AIRR rearrangements file into a data frame

    Arguments:
      handle (file): input file handle.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      pandas.DataFrame: Rearrangement records as rows of a data frame.
    """
    # TODO: test pandas.DataFrame.read_csv with converters argument as an alterative
    reader = RearrangementReader(handle, debug=debug)
    return pd.DataFrame(list(reader))


def write(dataframe, handle, debug=False):
    """
    Write the contents of a data frame to an AIRR rearrangements file

    Arguments:
      dataframe (pandas.DataFrame): data frame of rearrangement data.
      handle (file): output file handle.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if the file is written without error.
    """
    # TODO: test pandas.DataFrame.write_csv with converters argument as an alterative
    fields = dataframe.columns.tolist()
    writer = RearrangementWriter(handle, fields=fields, debug=debug)

    try:
        for __, row in dataframe.iterrows():
            writer.write(row.to_dict())
    except:
        raise

    return True

def merge(out_file, airr_files, drop=False, debug=False):
    """
    Merge one or more AIRR rearrangements files

    Arguments:
      out_file (str): output file name.
      airr_files (list): list of input files to merge.
      drop (bool): drop flag. If True then drop fields that do not exist in all input
                   files, otherwise combine fields from all input files.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files were successfully merged, otherwise False.
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

        out_handle = open(out_file, 'w')
        writer = RearrangementWriter(out_handle, fields=out_fields, debug=debug)

        for reader in readers:
            for rec in reader:
                writer.write(rec)

        out_handle.close()
    except:
        return False

    return True

def validate(airr_files, debug=False):
    """
    Validates one or more AIRR rearrangements files

    Arguments:
      airr_files (list): list of input files to validate.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      boolean: True if all files passed validation, otherwise False
    """
    valid = True
    for file in airr_files:
        print('Validating: %s' % os.path.basename(file))
        reader = RearrangementReader(open(file, 'r'))
        valid &= reader.validate()

    return valid
