#------------------------------------------------------------------------------
# HOW TO USE
# Step #1: Get track info using this file
# Step #2: Based on track info, set flags in change-language.py and run it
#------------------------------------------------------------------------------

import subprocess
import sys
from pathlib import Path

#------------------------------------------------------------------------------
# PART 0: Define global constants
#------------------------------------------------------------------------------

# Set MKVToolnix installation directory
mkvtoolnix_path = Path(r"C:\Program Files", "MKVToolNix")

# Set file extension
file_ext = ".mkv"


#------------------------------------------------------------------------------
# PART 1: Get track info for the mkv file in question
#------------------------------------------------------------------------------

# Input file location
input_file_str = input("\nEnter full file path: ")

# Clean up input string
if (input_file_str.startswith('"') == True 
    and input_file_str.endswith('"') == True):
    input_file = Path(input_file_str[1:-1])
else:
    input_file = Path(input_file_str)

# Show mkv track info for input file
if input_file.exists() == False:
    print(f"ERROR: Specified path ({input_file}) does not exist!")
    sys.exit()
else:
    subprocess.run([Path(mkvtoolnix_path, "mkvinfo.exe"), input_file])