"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

from airr.formats import RearrangementsFile


def read(filename):
    """Open an AIRR rearrangements file and read its contents"""
    return RearrangementsFile(filename, False)


def create(filename):
    """Create an empty AIRR rearrangements file"""
    return RearrangementsFile(filename, True)


def createDerivation(inputFilename, outputFilename, toolEntity, activity,
                     namespace, namespaceURI):
    """Create a derived AIRR rearrangments file, possibly with addl annotation
    fields
    """
    ifile = RearrangementsFile(inputFilename, False)
    ofile = RearrangementsFile(outputFilename, True)
    ofile.deriveFrom(ifile)
    ofile.addAnnotationActivity(inputFilename, outputFilename, toolEntity, activity, None, namespace, namespaceURI)
    return [ifile, ofile]


# versioneer-generated
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
