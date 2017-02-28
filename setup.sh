#!/bin/sh
git submodule init
git submodule update
cd pgoapi
python setup.py build
pip install -U  -r requirements.txt
cd ..
ls