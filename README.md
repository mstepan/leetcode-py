# Leetcode solution using Python 3

All solved tasks located inside `medium` package.

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
black .
```

### Linter

As a linter we will use [Flake8](https://flake8.pycqa.org/en/latest/)

To run linter use:

```bash
flake8 medium/
```