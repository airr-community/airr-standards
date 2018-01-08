AIRR Standards Development Process
----------------------------------

The airr-standards repository contains numerous sub-projects within it
which are all highly interconnected. Our goal is a simple workflow for
development that also insures stable versioning and releases for AIRR
data and software associated with publications and database
submissions. The current sub-projects include:

* Minimum information about an Adaptive Immune Receptor Repertoire Sequencing Experiment (MiAIRR).

* Specification of file formats:

1. Alignment hit table

2. Rearrangement annotations

* OpenAPI definitions:

1. MiAIRR objects

2. Rearrangement annotations

* Documentation for http://docs.airr-community.org

* Python package for reading/writing file formats

Some future sub-projects include:

* Ontologies definitions for AIRR data elements.

* Common Repository WG defining standard API with associated specification.

* R package for file format reading/writing/validation.

* Germline Database WG defining criteria, submission protocols, and
  tools, with associated file formats and specifications.

* Software WG defining standardized data sets and metrics.

### Git Structure

The `master` branch is utilized for all development for the ongoing
major version of the AIRR Standards. The versioning system, described
in separate section below, is designed to allow parallel branches of
development and maintenance for multiple AIRR Standards, though
currently there is a single version available, MiAIRR V1. When
multiple major versions of the AIRR Standards are available, then
these instructions will be updated to reflect the development process
for older versions.

* Commits to `master` can only be performed by the core team, which
  currently includes Syed Ahmad Chan Bukhari, Christian Busse, Scott
  Christley, Jason Vander Heiden, and Uri Laserson. Even so, consider
  using a pull request if the changes affect important MiAIRR or
  specifications files that may impact others. The core team will be
  expanded as the number of sub-projects in airr-standards grows.

* The priority is not to break `master` for other developers, this
  includes renaming or deleting fields, changing schema structure, or
  specification definitions. This type of work requires review by the
  core team.

* Members not on the core team should submit all changes as a pull
  request. This implies creating a feature branch to hold your
  changes, or forking the repository. Please use a meaningful unique
  name for your branch; these branches will be removed once merged
  into `master` and have stabilized.

* Our goal is for `master` never to be broken. Pull requests must pass
  checks before being merged.

* Use `rebase` instead of `merge` for either bringing your feature
  branch up-to-date with the latest `master` or when merging pull
  requests into `master`. The goal is for the commit history to be a
  tree (i.e. a single linear commit history to any specific release),
  versus a directed acyclic graph (DAG) with multiple commit
  paths. Using `git merge` can create these multiple commit paths.

* Issues do not have to be created for features as discussion can be
  attached to the pull request. However, if you wish to discuss
  design/implementations ideas beforehand, please feel free to create
  an issue.

We have a slack channel setup for GitHub notifications that are more
extensive than the normal email notifications. Please contact the core
team to be added.

### Versioning and Release Process

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

* MAJOR = MiAIRR version

* MINOR = Implementation specifications

* PATCH = Software updates

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
branch for every new PATCH release. When development on `master` is
deemed ready for release, a branch is created from `master` called
release-MAJOR.MINOR where MAJOR.MINOR.0 will be the first associated
release tag. The `master` branch will then be development for a future
MAJOR.MINOR release, for example if the current release branch is
release-1.1, then the `master` branch will be development for a future
1.2.0 or 2.0.0 release. All work related to a prior MAJOR.MINOR
release, which essentially should only be software updates and bug
fixes, should be commited to that release branch. Note: a release may
just tag `master` and not create the actual release branch until later
when it is needed.

### Code Style

**General Guidelines**

* Do not commit `.gitignore` files or IDE project files.

**Python**

* Follow [PEP8](https://www.python.org/dev/peps/pep-0008)
* Use [Google style docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
  for inline documentation.

**R**

* Follow the [Bioconductor style](https://bioconductor.org/developers/how-to/coding-style/),
  except use `snake_case` for variable names and a single `#` for comments.
* Use [roxygen2](https://github.com/klutometis/roxygen) for inline
  documentation and namespace management.