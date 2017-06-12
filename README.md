# airr-formats
Open source formats for AIRR data using Thrift.

Each specification is in a pair of files in `specs/`

-   `object.yaml`: A machine-readable set of fields

-   `object.j2`: A Markdown Jinja2 template with additional information


To render the specs, from the root package directory run

```bash
scripts/build_docs.sh
```

which will generate Markdown `.md` files in the `docs/` directory.  (This makes
use of the `jinja2-cli` package.)


All libraries are in the `lang/` subdirectory.
