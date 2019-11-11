#!/usr/bin/env bash

mkdir -p 'ai42'
cp *.py README.md LICENSE ./ai42 
python setup.py sdist bdist_wheel
