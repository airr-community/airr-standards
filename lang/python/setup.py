"""
AIRR community formats for adaptive immune receptor data.
"""

import sys
import os
import versioneer
from setuptools import setup, find_packages

try:
    from setuptools import setup
except ImportError:
    sys.exit('setuptools is required.')

try:
    from pip.req import parse_requirements
except ImportError:
    sys.exit('pip is required.\n')

with open('README.md', 'r') as ip:
    long_description = ip.read()

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
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='AIRR Community',
      author_email='',
      description='AIRR community formats for antibody and TCR sequence data.',
      long_description=long_description,
      zip_safe=False,
      license='MIT',
      url='http://docs.airr-community.org',
      keywords=('AIRR bioinformatics immunoglobulin antibody adaptive immune lymphocyte sequencing TCR CDR3'),
      install_requires=install_requires,
      packages=find_packages(),
      package_data={'airr': ['specs/*.yaml']},
      classifiers=['Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Bio-Informatics'])
