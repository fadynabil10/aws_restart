#write python code to print Adam's English degree from students.json file.
#cat students.json

#Answer


# Python program to read
# json file
import json

# Opening JSON file
f = open('students.json')

# returns JSON object as
# a dictionary
data = json.load(f)
print(data)
adam = data['adam']['english']
print (adam)
# Closing file
f.close()
