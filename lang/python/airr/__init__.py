"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

# Python packages
from __future__ import print_function
import sys

from . import airr_format

def read(filename):
    """Open an AIRR rearrangements file and read its contents"""
    return airr_format.Rearrangements(filename, False)

def create(filename):
    """Create an empty AIRR rearrangements file"""
    return airr_format.Rearrangements(filename, True)

def createDerivation(inputFilename, outputFilename, toolEntity, activity, namespace, namespaceURI):
    """Create a derived AIRR rearrangments file, possibly with additional annotation fields"""
    ifile = airr_format.Rearrangements(inputFilename, False)
    ofile = airr_format.Rearrangements(outputFilename, True)
    ofile.deriveFrom(ifile)
    ofile.addAnnotationActivity(inputFilename, outputFilename, toolEntity, activity, None, namespace, namespaceURI)
    return [ifile, ofile]
