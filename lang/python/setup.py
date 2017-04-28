#!/usr/bin/env python
"""
AIRR community V(D)J assignment data standard
"""
# Imports
import os
import sys

try:
    from setuptools import setup
except ImportError:
    sys.exit('Please install setuptools before installing airr.\n')

try:
    from pip.req import parse_requirements
except ImportError:
    sys.exit('Please install pip before installing airr.\n')

# Get version, author and license information
info_file = os.path.join('airr', 'version.py')
__version__, __author__, __license__ = None, None, None
try:
    exec(open(info_file).read())
except:
    sys.exit('Failed to load package information from %s.\n' % info_file)

if __version__ is None:
    sys.exit('Missing version information in %s\n.' % info_file)
if __author__ is None:
    sys.exit('Missing author information in %s\n.' % info_file)
if __license__ is None:
    sys.exit('Missing license information in %s\n.' % info_file)

# Load long package description
#desc_files = ['README.rst', 'INSTALL.rst', 'NEWS.rst']
desc_files = ['README.md']
long_description = '\n\n'.join([open(f, 'r').read() for f in desc_files])

# Define installation path for commandline tools
#scripts = ['vdjml_merge.py',
#           'igblast_tsv_merge.py',
#           'Cdr3_clone_identifier.py']

# TODO: check pip version to avoid problem with parse_requirements(session=False)
# Parse requirements
if os.environ.get('READTHEDOCS', None) == 'True':
    # Set empty install_requires to get install to work on readthedocs
    install_requires = []
else:
    require_file = 'requirements.txt'
    try:
        requirements = parse_requirements(require_file, session=False)
    except TypeError:
        requirements = parse_requirements(require_file)
    install_requires = [str(r.req) for r in requirements]

# Setup
setup(name='airr',
      version=__version__,
      author=__author__,
      author_email=__email__,
      description='AIRR community standard for V(D)J assignment results.',
      long_description=long_description,
      zip_safe=False,
      license=__license__,
      url='https://vdjserver.org',
      download_url='https://github.com/airr-community/airr-formats.git',
      keywords='AIRR bioinformatics immunoglobulin lymphocyte sequencing TCR CDR3',
      install_requires=install_requires,
      packages=['airr'],
      package_dir={'airr': 'airr'},
      package_data={'airr': ['rearrangements.yaml']},
      #scripts=scripts,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Scientific/Engineering :: Bio-Informatics'])
