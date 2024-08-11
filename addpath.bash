#!/bin/bash

# Get the directory of the current script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Define the output file path
OUT_FILE="$SCRIPT_DIR/out.tmp"

# Call your Python script (assuming it's named addPath.py)
python3 addPath.py "$@" --OUT "$OUT_FILE"

# Check if the output file exists
if [ -f "$OUT_FILE" ]; then
  # Read the content of the output file
  while IFS= read -r line; do
    # Append the line to PATH (if not empty)
    if [[ ! -z "$line" ]]; then
      export PATH="$PATH:$line"
    fi
  done < "$OUT_FILE"
  # Remove the temporary file quietly
  rm -f "$OUT_FILE"
fi

# Equivalente de addPath.bat generado por https://gemini.google.com/