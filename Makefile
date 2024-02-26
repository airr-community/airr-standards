# helper commands for keeping the language directories in sync

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help:
	@echo ""
	@echo "Helper commands for AIRR Standards repository"
	@echo ""
	@echo "make gen-v2       -- Generate OpenAPI V2 spec from the V3 spec"
	@echo "make build-docs   -- Build documentation"
	@echo "make spec-copy    -- Copy spec files to language directories"
	@echo "make data-copy    -- Copy test data files to language directories"
	@echo "make checks       -- Run consistency checks on spec files"
	@echo "make tests        -- Run all language test suites"
	@echo "make python-tests -- Run Python test suite"
	@echo "make r-tests      -- Run R test suite"
	@echo "make js-tests     -- Run Javascript test suite"
	@echo ""

gen-v2:
	@echo "Not implemented"

build-docs:
	sphinx-build -a -E -b html docs docs/_build/html

spec-copy:
	@echo "Copying specs to language directories"
	cp specs/airr-schema.yaml lang/python/airr/specs
	cp specs/airr-schema-openapi3.yaml lang/python/airr/specs
	cp specs/airr-schema.yaml lang/R/inst/extdata
	cp specs/airr-schema-openapi3.yaml lang/R/inst/extdata
#	cp specs/airr-schema.yaml lang/js/
#	cp specs/airr-schema-openapi3.yaml lang/js/

data-copy:
	@echo "Copying test data to language directories"
	cp tests/data/* lang/python/tests/data
	cp tests/data/* lang/R/tests/data-tests

checks:
	@echo "Running consistency checks on spec files"
	python3 tests/check-consistency-formats.py

tests: python-tests r-tests js-tests

python-tests:
	@echo "Running Python test suite"
	cd lang/python; python3 -m unittest discover

r-tests:
	@echo "Running R test suite"
	cd lang/R; R -e "library(devtools); test()"

js-tests:
	@echo "Running Javascript test suite"
