# Leetcode solution using Python 3.11

All solved tasks located inside `medium` package.

### Python version and virtual environment

We will use python 3.11.x for all our code.

To create virtual environment with all the dependencies use:

```bash
make setup
```

#### Freeze dependencies

Run the following command to freeze all dependencies:

```bash
make freeze
```

### Code Formatter

[Black](https://github.com/psf/black) will be used as a default code formatter.

To format current folder use:

```bash
make code_format
```

### Linter

As a linter we will use [Flake8](https://flake8.pycqa.org/en/latest/)

To run linter use:

```bash
make lint
```

### Unit tests with coverage

For unit tests we will use [pytest](https://docs.pytest.org/en/8.2.x/)
For code coverage we will use [coverage]().

To run all unit-tests with coverage reports execute:

```bash
make test
```