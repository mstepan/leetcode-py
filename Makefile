# Variables
VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
TESTS := tests
SRC := leetcode/

# Default target: create virtual environment and install dependencies
.PHONY: all
all: code_format lint test

.PHONY: setup
setup: create_venv install_dependencies

# Create virtual environment
.PHONY: create_venv
create_venv:
	python3 -m venv $(VENV_DIR)

# Install dependencies from requirements.txt
.PHONY: install_dependencies
install_dependencies: create_venv
	$(PIP) install -r requirements.txt

# Freeze PIP dependencies
.PHONY: freeze
freeze: activate
	$(PIP) freeze >  requirements.txt

# Activate virtual environment
.PHONY: activate
activate:
	. .venv/bin/activate

# Code formatting using black
.PHONY: code_format
code_format: activate
	$(PYTHON) -m black $(SRC)

# Execute flake8 linter
lint: activate
	$(PYTHON) -m flake8 $(SRC) --count --select=E9,F63,F7,F82 --show-source --statistics
	$(PYTHON) -m flake8 $(SRC) --count --exit-zero --max-complexity=10 --max-line-length=127 --ignore=E203 --statistics

# Run unit test with pytest and code coverage
.PHONY: test
test: activate
	$(PYTHON) -m coverage run -m pytest $(TESTS)
	$(PYTHON) -m coverage report
	$(PYTHON) -m coverage html

# Run flask application locally
.PHONY: run
run: activate
	$(PYTHON) -m app.py

# Clean up virtual environment and all other unnecessary files
.PHONY: clean
clean:
	rm -rf $(VENV_DIR) __pycache__ *.pyc *.pyo .pytest_cache


