# airr-formats

[![Build Status](https://travis-ci.org/airr-community/airr-formats.svg?branch=master)](https://travis-ci.org/airr-community/airr-formats)

Open source formats for AIRR data.

Each specification is in a pair of files in `specs/`

-   `object.yaml`: A machine-readable set of fields

-   `object.j2`: A Markdown Jinja2 template with additional information

To propagate specs from `specs/` into the packages in `lang/`, run

```bash
scripts/propagate-specs.sh
```

To render the specs, first install [`jinja2-cli`](https://pypi.python.org/pypi/jinja2-cli).

Then run from the root repo directory

```bash
scripts/build-docs.sh
```

which will generate Markdown `.md` files in the `docs/` directory.

All libraries are in the `lang/` subdirectory.
