"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""
from airr.io import RearrangementReader, RearrangementWriter


def read(handle, debug=False):
    """
    Open an AIRR rearrangements file and read its contents

    Arguments:
      handle (file): input file handle.
      debug (bool): debug flag. If True print debugging information to standard output.

    Returns:
      airr.io.RearrangementReader: open reader class.
    """
    return RearrangementReader(handle, debug=debug)


def create(handle, fields=None, debug=False):
    """
    Create an empty AIRR rearrangements file

    Arguments:
      handle (file): output file handle.
      fields (list): additional non-mandatory fields to add to the output.
      debug (bool): debug flag. If True print debugging information to standard output.

    Returns:
      airr.io.RearrangementWriter: open writer class.
    """
    return RearrangementWriter(handle, fields=fields, debug=debug)


def derive(out_handle, in_handle, fields=None, debug=False):
    """
    Create an empty AIRR rearrangements file with fields derived from an existing fiel

    Arguments:
      out_handle (file): output file handle.
      in_handle (file): existing file to derive fields from
      fields (list): additional non-mandatory fields to add to the output.
      debug (bool): debug flag. If True print debugging information to standard output.

    Returns:
      airr.io.RearrangementWriter: open writer class.
    """
    reader = RearrangementReader(in_handle)
    in_fields = list(reader.fields)
    if fields is not None:
        in_fields.extend([f for f in fields if f not in in_fields])
    return RearrangementWriter(out_handle, fields=in_fields, debug=debug)


# versioneer-generated
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
