#!/bin/bash

# Get the directory of the current script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Define output file path
OUTPUT_FILE="$SCRIPT_DIR/out.tmp.sh"

# Call your Python script with arguments and redirect output to the temporary file
python3 addPath.py "$@" --o "$OUTPUT_FILE"

# Check if the temporary file exists
if [ -f "$OUTPUT_FILE" ]; then
  # Execute the contents of the temporary file
  source "$OUTPUT_FILE"
  # Delete the temporary file
  rm -f "$OUTPUT_FILE"
fi

# No need to explicitly unset variables in Bash

sleep 2

# Equivalente de addPath.bat generado por https://gemini.google.com/
