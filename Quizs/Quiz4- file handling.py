# Quiz4 - file handling

lines = []
with open("file1.txt", 'r') as fp:
    lines = fp.readlines()

with open("file1.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        if number not in [3,6]:
            fp.write(line)