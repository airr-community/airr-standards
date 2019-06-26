==================================
AIRR Standards Development Process
==================================


Sub-Projects
============

The airr-standards repository contains numerous sub-projects within it
which are all highly interconnected. Our goal is a simple workflow for
development that also insures stable versioning and releases for AIRR
data and software associated with publications and database
submissions. The current sub-projects include:

-  Minimum information about an Adaptive Immune Receptor Repertoire
   Sequencing Experiment (MiAIRR).

-  Specification of file formats:

   1. Alignment hit table

   2. Rearrangement annotations

-  OpenAPI definitions:

   1. MiAIRR objects

   2. Rearrangement annotations

-  Documentation for `docs.airr-community.org`__

-  Python package for reading/writing file formats

.. __: http://docs.airr-community.org

Some future sub-projects include:

-  Ontologies definitions for AIRR data elements.

-  Common Repository WG defining standard API with associated
   specification.

-  R package for file format reading/writing/validation.

-  Germline Database WG defining criteria, submission protocols, and
   tools, with associated file formats and specifications.

-  Software WG defining standardized data sets and metrics.


Git Structure
=============

The ``master`` branch is utilized for all development for the ongoing
major version of the AIRR Standards. The versioning system, described
in separate section below, is designed to allow parallel branches of
development and maintenance for multiple AIRR Standards, though
currently there is a single version available, MiAIRR V1. When
multiple major versions of the AIRR Standards are available, then
these instructions will be updated to reflect the development process
for older versions.

-  Commits to ``master`` can only be performed by the core team, which
   currently includes Syed Ahmad Chan Bukhari, Christian Busse, Scott
   Christley, Jason Vander Heiden, and Uri Laserson. Even so, consider
   using a pull request if the changes affect important MiAIRR or
   specifications files that may impact others. The core team will be
   expanded as the number of sub-projects in airr-standards grows.

-  The priority is not to break ``master`` for other developers, this
   includes renaming or deleting fields, changing schema structure, or
   specification definitions. This type of work requires review by the
   core team.

-  Members not on the core team should submit all changes as a pull
   request. This implies creating a feature branch to hold your
   changes, or forking the repository. Please use a meaningful unique
   name for your branch; these branches will be removed once merged
   into ``master`` and have stabilized.

-  Our goal is for ``master`` never to be broken. Pull requests must
   pass checks before being merged.

-  Use ``rebase`` instead of ``merge`` for either bringing your feature
   branch up-to-date with the latest ``master`` or when merging pull
   requests into ``master``. The goal is for the commit history to be a
   tree (i.e. a single linear commit history to any specific release),
   versus a directed acyclic graph (DAG) with multiple commit
   paths. Using ``git merge`` can create these multiple commit paths.

-  Issues do not have to be created for features as discussion can be
   attached to the pull request. However, if you wish to discuss
   design/implementations ideas beforehand, please feel free to create
   an issue.

We have a slack channel setup for GitHub notifications that are more
extensive than the normal email notifications. Please contact the core
team to be added.


Versioning and Release Process
==============================

Versions and associated releases are driven by the recommendations and
standards produced by the AIRR Community and their associated Working
Groups, with specifications and software tools implementing those
recommendations and standards. The various sub-projects within
airr-standards do not have independent versioning but are
interconnected together through the same version numbers. This way
users know exactly which software versions are associated with which
standards versions. This has the challenge that normal semantic
version numbering (MAJOR.MINOR.PATCH) cannot be applied to the
sub-projects, however the goal is that semantic versioning will apply
to AIRR Standards as a whole. The design is thus:

-  MAJOR = MiAIRR version

-  MINOR = Implementation specifications

-  PATCH = Software updates

New and updated software tools will generally increment the PATCH
number, assuming that the implementation specifications have not
changed. The current MiAIRR version is V1 (i.e. MAJOR = 1), and it is
expected that this version will rarely change as it required formal
adoption by the AIRR Community. Currently, MINOR = 0 as the
implementation specifications are in pre-release form going through
many changes. Once they are released (i.e. v1.1.0) then MINOR will be
incremented whenever a backwards incompatible change is introduced.

The airr-standards repository uses release branches to maintain stable
releases separate from ongoing development. Each release branch is for
a specific MAJOR.MINOR version, with tags being assigned on that
branch for every new PATCH release. When development on ``master`` is
deemed ready for release, a branch is created from ``master`` called
release-MAJOR.MINOR where MAJOR.MINOR.0 will be the first associated
release tag. The ``master`` branch will then be development for a future
MAJOR.MINOR release, for example if the current release branch is
release-1.1, then the ``master`` branch will be development for a future
1.2.0 or 2.0.0 release. All work related to a prior MAJOR.MINOR
release, which essentially should only be software updates and bug
fixes, should be commited to that release branch. Note: a release may
just tag ``master`` and not create the actual release branch until later
when it is needed.

Public Releases
---------------

To provide a public release of the airr-standards library, perform the
following checklist:

-  Tag the repository
-  Generate the release on github
-  Upload python library to PyPI
-  Upload R library to CRAN

To upload the python library to PyPI, perform the following steps:

-  something
-  something

To upload the R library to CRAN, perform the following steps:

-  something
-  something


Development Setup
=================

Local development and testing can be performed either directly in your machine
environment, or you can use a docker container which avoids conflicts with other
software. For all cases, you will want a local copy of the github repository.

.. code-block:: bash

  git clone https://github.com/airr-community/airr-standards.git

If you will be working in a docker container, you can pull down the airr-standards
image, which has all of the prerequisites installed, or you can use your own image.
The airr-standards image provides a python3 environment.

.. code-block:: bash

  docker pull airrc/airr-standards

You will want to mount your local copy of the github repository into the container.
This example command puts your local copy at the ``/work`` directory. Note that a copy
of the repository exists in the image from when it is built, but don't edit that copy
as your changes will get lost when you exist the docker container. It is suggested
that you edit files outside of the docker container to prevent permissions issues. Also,
avoid doing ``git`` commands inside the docker container. Certains commands that write
data like ``git add`` or ``git commit`` can change permissions and make your local
copy of the repository unusable.

.. code-block:: bash

  cd airr-standards
  docker run -v $PWD:/work -it airrc/airr-standards bash

Python Library
--------------

Normal users would install the python library using ``pip`` which pulls the package
from the internet. For development, you want to install from your local copy. The
commands are similar whether in docker or directly in your machine environment.
Starting at the top level repository directory:

.. code-block:: bash

  cd lang/python
  python setup.py install

If you are working directly in your machine environment, you may want to install in your
user site packages instead of the system site packages, which can be done by adding
the ``--user`` option to the install.

.. code-block:: bash

  python setup.py install --user

You can run the python test suite from the same directory where you do the install command.

.. code-block:: bash

  python -m unittest discover

R Library
---------

Documentation
-------------

The documentation at `docs.airr-community.org` is built using ``sphinx`` in a python3
environment. From the top level airr-standards directory, run this command to build a
local version of the website.

.. code-block:: bash

  sphinx-build -a -E -b html docs docs/_build/html

The documentation can then be viewed in your browser by opening the file ``docs/_build/html/index.html``.


Code Style
==========

General Guidelines
------------------

-  Do not commit ``.gitignore`` files or IDE project files.

Python
------

-  Follow `PEP8`_.
-  Use `Google style docstrings`_ for inline documentation.

.. _`PEP8`: https://www.python.org/dev/peps/pep-0008
.. _`Google style docstrings`: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

R
---

-  Follow the `Bioconductor style`_, except use ``snake_case`` for
   variable names and a single `#` for comments.
-  Use `roxygen2`_ for inline documentation and namespace management.
  
.. _`Bioconductor style`: https://bioconductor.org/developers/how-to/coding-style/
.. _`roxygen2`: https://github.com/klutometis/roxygen
