"""
Interface functions for file operations
"""
# System imports
import sys
import pandas as pd
from collections import OrderedDict
from itertools import chain

# Load imports
from airr.io import RearrangementReader, RearrangementWriter
from airr.schema import ValidationError, RearrangementSchema


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
    Validates one or more AIRR rearrangements files

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
