#!/bin/bash

# Find all files named main.py in the current directory and all subdirectories
find "$(dirname "$0")" -type f -name "main.py" | while read -r file; do
    echo "Adding $file to git"
    git add "$file"
done
