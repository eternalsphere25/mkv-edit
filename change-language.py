#------------------------------------------------------------------------------
# HOW TO USE
# Step #1: Get track info using get-track-info.py
# Step #2: Based on track info, set flags below, then run this file
#------------------------------------------------------------------------------

import subprocess
from pathlib import Path


#------------------------------------------------------------------------------
# PART 0: Define global constants
#------------------------------------------------------------------------------

# Set MKVToolnix installation directory
mkvtoolnix_path = Path(r"C:\Program Files", "MKVToolNix")

# Set file extension
file_ext = ".mkv"


#------------------------------------------------------------------------------
# PART 1: Figure out which files are MKV files
#------------------------------------------------------------------------------

# Enter directory with files
input_dir_str = input("\nEnter full file path of directory containing files: ")

# Clean up input string
if (input_dir_str.startswith('"') == True 
    and input_dir_str.endswith('"') == True):
    input_file_dir = Path(input_dir_str[1:-1])
else:
    input_file_dir = Path(input_dir_str)

# Get list of files in folder
file_list  = [x for x in input_file_dir.iterdir() if x.is_file()
              and x.suffix==file_ext.casefold()]

# Input command and break up into list
args = (f"--edit track:2 --set flag-default=0 --edit track:3 "
        f"--set flag-default=1 --edit track:4 --set flag-default=0")
args = args.split(" ")

# Run batch conversion
for item in file_list:
    print(f"\nProcessing file: {item}")
    program = [Path(mkvtoolnix_path, "mkvpropedit.exe"), item]
    command = program + args
    subprocess.run(command)