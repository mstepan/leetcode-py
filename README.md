# Leetcode solution using Python 3

All solved tasks located inside `medium` package.


### Python version and virtual environment

We will use python 3.11.x for all code.

To install virtual environment use:
```bash
python3.11 -m venv .venv/
```

### Dependency Management

We will use virtual environment to install all required dependencies.

#### To install all required dependencies do the following:

1. Active python virtual environment.

```bash
source .venv/bin/activate
```

2. Install all dependencies using `pip`

```bash
pip install -r requirements.txt
```

#### Freeze dependencies

Run the following command to freeze all dependencies:

```bash
pip freeze > requirements.txt
```

### Code Formatter

[Black](https://github.com/psf/black) will be used as a default code formatter.

To format current folder use:

```bash
black --line-length 120 .
```

### Linter

As a linter we will use [Flake8](https://flake8.pycqa.org/en/latest/)

To run linter use:

```bash
flake8 medium/
```

### Unit tests

For unit tests we will use [pytest](https://docs.pytest.org/en/8.2.x/)

To run all unit-tests execute:

```bash
pytest
```

### Code Coverage

For code coverage we will use [coverage]().

To gather code coverage, execute the following script:

```bash
./run_coverage.sh
```

To view aggregated report as html execute:

```bash
coverage html

open htmlcov/index.html
```