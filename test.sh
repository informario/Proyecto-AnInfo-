#!/bin/bash

# Use:
# chmod +x test.sh
# ./test.sh

python3 -m unittest menu.py > _test.txt
rm _test.txt

