#!/usr/bin/env bash
set -euxo pipefail

coverage run -m pytest
coverage report
