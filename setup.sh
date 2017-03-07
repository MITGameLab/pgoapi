#!/bin/sh
git submodule init
git submodule update
cd pgoapi
git submodule init
git submodule update
python setup.py build
pip install -r requirements.txt
cd ..
ls