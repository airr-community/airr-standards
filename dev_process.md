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

### Git Structure

The `master` branch is utilized for all development for the ongoing
major version of the AIRR Standards. The last major release was MiAIRR
v1.0 so all development work on `master` is for v1.X releases. When
multiple major versions of the AIRR Standards are available, then
these instructions will be updated to reflect the development process for
older versions.

* Submit all changes as a pull request.

* Pull requests must pass checks before being merged.

* No commits directly to `master` branch. With exception that the core
  team may do so for small changes that do not affect the
  outward-facing AIRR standards.

* Merges to `master` can only be performed by the core team, which
  currently includes Syed Ahmad Chan Bukhari, Christian Busse, Scott
  Christley, Jason Vander Heiden, and Uri Laserson.

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
to AIRR Standards as a whole. New and updated software tools will
increment the PATCH number, but the MAJOR and MINOR numbers will only
be incremented for changes to the AIRR Standards.

The airr-standards repository uses release branches to maintain stable
releases. When development on `master` is deemed ready for release, a
branch is created from master called release-vX.X.X where vX.X.X is
associated release. Any bug fixes related to the release can be
committed directly to the release branch, and when satified then the
branch is tagged with vX.X.X to finalize the source code
release. Additional work may occur as software tools are packaged and
posted to package management sites.

### Code Style

