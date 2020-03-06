#!/bin/sh

pip install --upgrade pip setuptools wheel
pip install --no-binary :all: nmslib
pip install .
pip install python-coveralls
