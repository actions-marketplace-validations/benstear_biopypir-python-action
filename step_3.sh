#!/bin/sh

pip install --upgrade pip setuptools wheel
pip install os
pip install time
pip install json
pip install pandas 
pip install tabulate 
pip install glob
pip install numpy 
python3 process_logs.py

