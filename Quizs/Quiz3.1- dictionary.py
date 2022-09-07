sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to extract
keys = ["name", "salary"]

#Output: {'name': 'Kelly', 'salary': 8000}

#Answer
mydict = {}
mydict = {keys[0]:sample_dict[keys[0]],keys[1]:sample_dict[keys[1]]}
print (mydict)