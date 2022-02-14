##########################################################################
#JSON storing & exchanging data between a web application and a server.
# Explanation on how to convert json into dictionary & pretty print in python:
# parse json string to various objects, python readables

import json

# Parse JSON - Convert from JSON -> to Python
print("1 ................ Convert from JSON -> to Python")
# json string
personJSON = '{ "name" : "Apollo","language" : "greek"}'

# If you have a JSON string, you can parse it by using the json.loads() method.
personPython = json.loads(personJSON)
# 1. print normal
print (personPython)
# 2. print languages
print (personPython['language'])


# Convert from Python -> to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
print("2 ................Convert from Python -> to JSON")
# a Python object (dict):
pythonDictionary = {
  "name": "Apollo",
  "age": 30,
  "city": "Delphi"
}

# convert into JSON:
jsonConverted = json.dumps(pythonDictionary)
# the result is a JSON string:
print(jsonConverted)


# read a JSON file
print ("3 ................read a JSON file")
with open ("data.json") as f :
    data = json.load(f)
    print(data)


# generate a NEW json FILE containing python values
print ("4 ................generate a NEW json FILE containing python values")
pythonDictionary = {"key1" : "value1",
                    "key2" : "value2"}

with open('my_file.txt', 'w') as json_file : # open file in write mode, created
    json.dump(pythonDictionary, json_file) # transform dict in json string

# to debug & analize json file - pretty print:
with open ("data.json") as f:
    data = json.load(f)
    print ("crapy format : ")
    print(data)

    print ("now, pretty print : ")
    print (json.dumps(data, indent = 4, sort_keys = True))
