# helper commands for keeping the language directories in sync

# Get schema version
AIRR_SCHEMA_VERSION=v$(shell python3 -c 'import yaml; x=yaml.safe_load(open("specs/airr-schema-openapi3.yaml","r")); print(x["Info"]["version"])')

# note: "help" MUST be the first target in the file, so
# when the user types "make" they get help info by default
help:
	@echo ""
	@echo "Helper commands for AIRR Standards repository"
	@echo "---------------------------------------------"
	@echo ""
	@echo "make spec-copy       -- Copy spec files to language directories"
	@echo "make data-copy       -- Copy test data files to language directories"
	@echo ""
	@echo "make docker-latest   -- Build docker image with latest tag"
	@echo "make docker-$(AIRR_SCHEMA_VERSION)    -- Build docker image with schema version: $(AIRR_SCHEMA_VERSION)"
	@echo ""
	@echo "  Example: docker run -v \$$PWD:/work -it airrc/airr-standards:latest bash"
	@echo "  Example: docker run -v \$$PWD:/work -it airrc/airr-standards:$(AIRR_SCHEMA_VERSION) bash"
	@echo ""
	@echo "  (environment setup required and/or run in docker)"
	@echo "make checks          -- Run consistency checks on spec files"
	@echo "make tests           -- Run all language test suites"
	@echo "make python-tests    -- Run Python test suite"
	@echo "make r-tests         -- Run R test suite"
	@echo "make js-tests        -- Run Javascript test suite"
	@echo ""
	@echo "make build-docs      -- Build documentation"
	@echo ""

build-docs:
	sphinx-build -a -E -b html docs docs/_build/html

docker-latest:
	@echo "Building latest docker image"
	docker build -f docker/Dockerfile -t airrc/airr-standards:latest .

docker-$(AIRR_SCHEMA_VERSION):
	@echo "Building $(AIRR_SCHEMA_VERSION) docker image"
	docker build -f docker/Dockerfile -t airrc/airr-standards:$(AIRR_SCHEMA_VERSION) .

spec-copy:
	@echo "Copying specs to language directories"
	cp specs/airr-schema.yaml lang/python/airr/specs
	cp specs/airr-schema-openapi3.yaml lang/python/airr/specs
	cp specs/airr-schema.yaml lang/R/inst/extdata
	cp specs/airr-schema-openapi3.yaml lang/R/inst/extdata
	cp specs/airr-schema-openapi3.yaml lang/js/

data-copy:
	@echo "Copying test data to language directories"
	cp tests/data/* lang/python/tests/data
	cp tests/data/* lang/R/tests/data-tests
	cp tests/data/* lang/js/tests/data

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
	cd lang/js; rm -rf node_modules; rm -rf coverage
	cd lang/js; npm install; npm run eslint; npm run test
