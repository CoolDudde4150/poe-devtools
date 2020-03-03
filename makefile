BUILD_DIR = build
DOCS_DIR = docs
SHELL = /bin/bash
PROTO_SRC = scripts/protobuf/src

.PHONY: help
help:
	@printf "\n%s" "Usage" \
			"make setup:			Setups the project to be developed on." \
			"make test_offline:		Uses pytest on all test files with the name formatted 'offline*test*.py'"\
			"make test_online:		Uses pytest on all test files with the name formatted 'online*test*.py'" \
			"make test:			Uses pytest on all tests found with either of the above name formats." \
			"make env:			Creates a python virtual environment with the necessary dependencies." \
			"make proto:			Compiles protobuf files and moves them into the required directory (based on relative path)" \
			"make docs:			Compiles the Sphinx documentation"
	@echo " "

.PHONY: setup
setup:
	make env
	source ./activate
	make proto

.PHONY: test_offline
test_offline:
	python -m pytest $(shell find . -name offline*test*.py)

.PHONY: test_online
test_online:
	python -m pytest $(shell find . -name online*test*.py)

.PHONY: test
test: test_offline test_online

.PHONY: env
env:
	@-rm -rf activate
	# TODO: Find a way to automatically recognize the version of python being used.
	@python3 -m venv env && \
	source env/bin/activate && \
	pip install -r requirements.txt && \
	ln env/bin/activate activate
	@printf "\n\n%s\n" "Use 'source ./activate' to enter the environment"

.PHONY: proto
proto:
	@echo "Making proto files."
	@for proto_file in $(shell find $(PROTO_SRC) -name *.proto); do \
		protoc $$proto_file -I $(PROTO_SRC) --python_out=.; \
	done
	@echo "Proto files automatically placed in the needed directories"

.PHONY: docs
docs:
	@cd $(DOCS_DIR) && make html