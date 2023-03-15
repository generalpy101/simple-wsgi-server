#!/bin/bash

printf "#/bin/sh\nblack ./src\ngit add ./src\npython lint.py -p ./src" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit