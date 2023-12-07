#!/bin/bash

# Use:
# chmod +x test.sh
# ./test.sh

python3 -m unittest menu.py > __test.txt
rm __test.txt

