"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

from airr.formats import RearrangementsFile


def read(handle, debug=False):
    """Open an AIRR rearrangements file and read its contents"""
    return RearrangementsFile(False, handle, debug=debug)


def create(handle, debug=False):
    """Create an empty AIRR rearrangements file"""
    return RearrangementsFile(True, handle, debug=debug)


def createDerivation(inputHandle, outputHandle, toolEntity, activity,
                     namespace, namespaceURI):
    """Create a derived AIRR rearrangments file, possibly with addl annotation
    fields
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
