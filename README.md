# airr-formats

Open source formats for AIRR data.

Each specification is in a pair of files in `specs/`

-   `object.yaml`: A machine-readable set of fields

-   `object.j2`: A Markdown Jinja2 template with additional information


To render the specs, first install [`jinja2-cli`](https://pypi.python.org/pypi/jinja2-cli).

Then run from the root package directory

```bash
scripts/build_docs.sh
```

which will generate Markdown `.md` files in the `docs/` directory.

All libraries are in the `lang/` subdirectory.
