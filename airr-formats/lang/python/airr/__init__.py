"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

from airr.formats import RearrangementsFile


def read(filename=None, handle=None, debug=False):
    """Open an AIRR rearrangements file and read its contents"""
    return RearrangementsFile(False, filename=filename, handle=handle, debug=debug)


def create(filename=None, handle=None, debug=False):
    """Create an empty AIRR rearrangements file"""
    return RearrangementsFile(True, filename=filename, handle=handle, debug=debug)


def createDerivation(inputFilename, outputFilename, toolEntity, activity,
                     namespace, namespaceURI):
    """Create a derived AIRR rearrangments file, possibly with addl annotation
    fields
    """
    ifile = RearrangementsFile(False, filename=inputFilename)
    ofile = RearrangementsFile(True, filename=outputFilename)
    ofile.deriveFrom(ifile)
    ofile.addAnnotationActivity(inputFilename, outputFilename, toolEntity, activity, None, namespace, namespaceURI)
    return [ifile, ofile]


# versioneer-generated
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
