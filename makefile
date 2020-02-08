BUILD_DIR = build
DOCS_DIR = docs
SHELL = /bin/bash

.PHONY: help
help:
	@printf "\n%s" "Usage" \
			"make test_offline:		Uses pytest on all test files with the name formatted 'offline*test*.py'"\
			"make test_online:		Uses pytest on all test files with the name formatted 'online*test*.py'" \
			"make test:			Uses pytest on all tests found with either of the above name formats." \
			"make env:			Creates a python virtual environment with the necessary dependencies." \
			"make proto:			Compiles protobuf files into a build directory. They need to be manually moved" \
			"make docs:			Compiles the Sphinx documentation"
	@echo " "

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
	python3 -m venv env && \
	source env/bin/activate && \
	pip install -r requirements.txt && \
	ln env/bin/activate activate
	@echo "\n\nUse 'source ./activate' to enter the environment\n"

.PHONY: proto
proto:
	@mkdir -p scripts/protobuf/$(BUILD_DIR)/
	@echo "Making proto files."
	@for proto_file in $(shell find . -name *.proto); do \
		protoc $$proto_file --python_out=scripts/protobuf/build; \
	done
	@echo "Proto files compiled. Find in scripts/protobuf/$(BUILD_DIR)"

.PHONY: docs
docs:
	@cd $(DOCS_DIR) && make html