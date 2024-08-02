#!/bin/bash

# Define the base directory to search in
base_dir=$(dirname "$0")

# Find and delete all memray-*.bin files in the current directory and all subdirectories
find "$base_dir" -type f -name "memray-*.bin" | while read -r file; do
    echo "Deleting $file"
    rm "$file"
done
