# Dictionary : Sequence of key:value pairs seperated with comma(,) which are declared inside { }..

dict1 = {"name":"ramesh","email":"ramesh@gmail.com","mobile":8284928926,"state":"Telangana"}


print(dict1)

# Accessing inside the dictionary is done using the name of the key which you want to access..

# [] - Its the symbol for accessing.

# print(dict1['email'])

# print(dict1['mobile'])


# Keys inside the dictionary should be immutable only..(integer,string,tuple)
# Values inside the dicitonary can be of any datatype..

# dict2 = {'name':'suresh',1:21,(1,2,3):[21,22,23]} # correct format

# dict2 = {'name':'suresh',1:21,(1,2,3):[21,22,23],[1,2,3]:"Sample"} # Error as u r declaring a mutuable element..

# print(dict2)


# Dictionaries are mutubale..


# dict1 = {"name":"ramesh","email":"ramesh@gmail.com","mobile":8284928926,"state":"Telangana"}

# dict1['country'] = "India" # If key not present in the dictinary it will be added as new key:value pair.

# print(dict1)

# dict1['state'] = "AndhraPradesh" # If the key is already present inside the dictionary, Previous key value will be updated with new value.

# print(dict1)


# Dictionary Keys are unique..

dict1 = {"name":"ramesh","email":"ramesh@gmail.com","mobile":8284928926,"state":"Telangana","mobile":329320920983}

# If we have repetition of same key in the dictionary, it will consider the latest key:value pair inside the dictionary..
print(dict1)


# print("mobile" in dict1)

# if 'city' in dict1: # This is for checking whwther the key is already existed in the dictionary.
#     pass
# else:
#     city = input("Enter your city")
#     dict1['city'] = city

# print(dict1)

# print(dict1['city'])


# print(dir(dict))

nested_dict = {"states":{"state1":"Andhrapradesh","state2":"Telanagan"}}