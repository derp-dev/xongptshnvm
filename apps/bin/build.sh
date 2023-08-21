#!/bin/bash
set -xe

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters. Please provide one argument."
    exit 1
fi

# Check if the argument is a single lowercase letter
if [[ $1 =~ ^[a-z]$ ]]; then
    # Check if the file exists
    if [[ -f "${1}func.c" ]]; then
        # Compile the C file
        gcc -Wall -Wextra -pedantic -std=ansi -o "${1}func.out" "${1}func.c" -v 2>&1
    else
        # If the file does not exist, create it and open in vi editor
        touch "${1}func.c"
        vi "${1}func.c"
    fi
else
    echo "Invalid argument. Please provide a single lowercase letter."
    exit 1
fi