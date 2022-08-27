library(markr)
library(airr)

doc_path <- "../../docs/packages/airr-R"
build_mkdocs(".", doc_path=doc_path, style="sphinx", yaml=F)
run_pandoc(doc_path, format="rst", delete=T)

# TODO: Post execution we still need to do cleanup:
# Edit the title and about in docs/packages/airr-R/overview.rst
# Remove the progress bar from the example in docs/*_tabular.rst and docs/ExampleData.rst
