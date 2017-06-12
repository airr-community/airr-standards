"""
AIRR community formats for adaptive immune receptor data.
"""

from setuptools import setup, find_packages
import versioneer


with open('README.md', 'r') as ip:
    long_description = ip.read()


# Setup
setup(name='airr-formats',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='AIRR Community',
      author_email='',
      description='AIRR community formats for antibody and TCR sequence data.',
      long_description=long_description,
      zip_safe=False,
      license='Apache v2',
      url='https://airr-formats.readthedocs.org/',
      keywords=('AIRR bioinformatics immunoglobulin antibody adaptive immune '
                'lymphocyte sequencing TCR CDR3'),
      install_requires=['pyyaml', 'prov'],
      packages=find_packages(),
      package_data={'airr': ['specs/*.yaml']},
      classifiers=['Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Bio-Informatics'])
