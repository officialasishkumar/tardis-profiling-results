#!/bin/bash

# Find all files named main.py in the current directory and all subdirectories
find "$(dirname "$0")" -type f -name "main.py" | while read -r file; do
    echo "Running memray on $file"
    memray run "$file"

    # Find the memray output file
    memray_file=$(find "$(dirname "$file")" -type f -name "memray-*.bin" -print -quit)
    
    if [ -n "$memray_file" ]; then
        echo "Found memray output: $memray_file"
        
        # Run the summary command
        memray summary "$memray_file" | tee "$(dirname "$memray_file")/summary-report-memray.txt"
        
        # Run the stats command
        memray stats "$memray_file" | tee "$(dirname "$memray_file")/stats-report-memray.txt"
    else
        echo "No memray output file found for $file"
    fi
    
    # Run scalene on the main.py file
    scalene "$file"
done
