"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""
from airr.interface import read, create, derive, load, write, merge, validate

# versioneer-generated
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
