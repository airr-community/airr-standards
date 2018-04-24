library(markr)
library(airr)

doc_path <- "../../docs/lang/R"
build_mkdocs(".", doc_path=doc_path, style="sphinx", yaml=F)
run_pandoc(doc_path, format="rst", delete=T)
