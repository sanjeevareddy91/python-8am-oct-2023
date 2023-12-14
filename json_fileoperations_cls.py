data = [{
    "name":"ramesh",
    "email":"ramesh@gmail.com",
    "mobile":"8392982893"
},
{
    "name":"ramesh",
    "email":"ramesh@gmail.com",
    "mobile":"8392982893"
},
{
    "name":"ramesh",
    "email":"ramesh@gmail.com",
    "mobile":"8392982893"
},
{
    "name":"ramesh",
    "email":"ramesh@gmail.com",
    "mobile":"8392982893"
}]


import json

# dumps
# dump

# load 
# loads


# loads -- Its for converting json string into python object..
# json_str = """[{
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893",
#     "city":null
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893",
#     "city":"Hyderabad"
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893",
#     "city":"Hyderabad"
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893",
#     "city":null
# }]"""

# print(json_str)
# print(type(json_str))
# # print(help(json.loads))

# py_object = json.loads(json_str)

# print(py_object)
# print(type(py_object))



# # dumps -- This is for converting python object into json str..

# py_object.append({'name': 'mahesh', 'email': 'mahesh@gmail.com', 'mobile': '784448845', 'city': "Chennai"})

# converted_str = json.dumps(py_object)

# print(converted_str)
# print(type(converted_str))

# print(help(json.load))

with open('sample_data.json') as file_object:
    json_data = json.load(file_object)

    # print(json_data)
    # print(type(json_data))

json_data.append({'name': 'venkatesh', 'email': 'venkatesh@gmail.com', 'mobile': '8377474743', 'city': "Bangalore"})

# dump() - -Its for adding the json data into the json file..

with open('write_data.json','w') as file_object:
    json.dump(json_data,file_object,indent=4)


# loads - converting string to python object..
# dumps - converting python obejct to strngs.

# load - load the json_file and considering the data into python object
# dump - considering the python object and saving it in json file..
