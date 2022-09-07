#write a python code to delete lines 3-6 from a text file.
#cat file1.txt

#Answer

import os

# list to store file lines
lines = []
# read file
with open(r"file2.txt", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()

# Write file
with open(r"file2.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 3 and 6. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in [2, 5]:
            fp.write(line)
