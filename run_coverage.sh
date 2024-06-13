#!/usr/bin/env bash
set -euxo pipefail

coverage run --source=medium -m pytest test/
coverage report
