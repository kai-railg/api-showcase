#!/bin/bash

# package from setup.py
python setup.py sdist bdist_wheel

# package from hatchling
hatchling build

# Upload to PyPI
pip install twine
twine upload --repository-url https://repo.westwell.cc/repository/cosmos-local/ dist/*
