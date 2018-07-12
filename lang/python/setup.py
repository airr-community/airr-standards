"""
AIRR community formats for adaptive immune receptor data.
"""
import sys
import os
import versioneer

try:
    from setuptools import setup, find_packages
except ImportError:
    sys.exit('setuptools is required.')

with open('README.rst', 'r') as ip:
    long_description = ip.read()

# Parse requirements
if os.environ.get('READTHEDOCS', None) == 'True':
    # Set empty install_requires to get install to work on readthedocs
    install_requires = []
else:
    with open('requirements.txt') as req:
        install_requires = req.read().splitlines()

# Setup
setup(name='airr',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='AIRR Community',
      author_email='',
      description='AIRR Community Data Representation Standard reference library for antibody and TCR sequencing data.',
      long_description=long_description,
      zip_safe=False,
      license='CC BY 4.0',
      url='http://docs.airr-community.org',
      keywords=['AIRR', 'bioinformatics', 'sequencing', 'immunoglobulin', 'antibody',
                'adaptive immunity', 'T cell', 'B cell', 'BCR', 'TCR'],
      install_requires=install_requires,
      packages=find_packages(),
      package_data={'airr': ['specs/*.yaml']},
      entry_points={'console_scripts': ['airr-tools=airr.tools:main']},
      classifiers=['Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Bio-Informatics'])
