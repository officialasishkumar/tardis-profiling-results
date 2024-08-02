#!/bin/bash

# Find all files named main.py in the current directory and all subdirectories
find "$(pwd)" -type f -name "main.py" | while read -r file; do
    abs_dir=$(dirname "$(realpath "$file")")

    # Change to the directory containing main.py
    cd "$abs_dir" || continue

    echo "Running memray on $file"
    memray run "$file"

    # Find the memray output file
    memray_file=$(find "$abs_dir" -type f -name "memray-*.bin" -print -quit)
    
    if [ -n "$memray_file" ]; then
        echo "Found memray output: $memray_file"
        
        # Run the summary command
        memray summary "$memray_file" | tee "$abs_dir/summary-report-memray.txt"
        
        # Run the stats command
        memray stats "$memray_file" | tee "$abs_dir/stats-report-memray.txt"
    else
        echo "No memray output file found for $file"
    fi
    
    # Run scalene on the main.py file
    scalene "$file"
done
