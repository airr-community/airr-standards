"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""
from airr.formats import RearrangementsFile


def read(handle, debug=False):
    """
    Open an AIRR rearrangements file and read its contents

    Arguments:
      handle (file): input file handle.
      debug (bool): debug flag. If True print debugging information to standard output.

    Returns:
      airr.RearrangementsFile:  RearrangementsFile object in read mode.
    """
    return RearrangementsFile(False, handle, debug=debug)


def create(handle, debug=False):
    """
    Create an empty AIRR rearrangements file

    Arguments:
      handle (file): output file handle.
      debug (bool): debug flag. If True print debugging information to standard output.

    Returns:
      airr.RearrangementsFile:  RearrangementsFile object in write mode.
    """
    return RearrangementsFile(True, handle, debug=debug)


def createDerivation(inputHandle, outputHandle, toolEntity, activity,
                     namespace, namespaceURI):
    """
    Create a derived AIRR rearrangments file

    Arguments:
      inputHandle (file): input file handle.
      outputHandle (file): output file handle.
      toolEntity (str): TODO
      activity (str): TODO
      namespace (str): TODO
      namespaceURI (str): TODO

    Returns:
      list: list of two airr.RearrangementsFile objects where the first
            object is the input reader and the second is the output writer.
    """
    ifile = RearrangementsFile(False, inputHandle)
    ofile = RearrangementsFile(True, outputHandle)
    ofile.deriveFrom(ifile)
    ofile.addAnnotationActivity(inputHandle.name, outputHandle.name, toolEntity, activity, None, namespace, namespaceURI)

    return [ifile, ofile]


# versioneer-generated
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
