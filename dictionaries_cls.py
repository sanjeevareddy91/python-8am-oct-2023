# # Dictionary : Sequence of key:value pairs seperated with comma(,) which are declared inside { }..

# dict1 = {"name":"ramesh","email":"ramesh@gmail.com","mobile":8284928926,"state":"Telangana"}


# # print(dict1)

# # Accessing inside the dictionary is done using the name of the key which you want to access..

# # [] - Its the symbol for accessing.

# # print(dict1['email'])

# # print(dict1['mobile'])


# # Keys inside the dictionary should be immutable only..(integer,string,tuple)
# # Values inside the dicitonary can be of any datatype..

# # dict2 = {'name':'suresh',1:21,(1,2,3):[21,22,23]} # correct format

# # dict2 = {'name':'suresh',1:21,(1,2,3):[21,22,23],[1,2,3]:"Sample"} # Error as u r declaring a mutuable element..

# # print(dict2)


# # Dictionaries are mutubale..


# # dict1 = {"name":"ramesh","email":"ramesh@gmail.com","mobile":8284928926,"state":"Telangana"}

# # dict1['country'] = "India" # If key not present in the dictinary it will be added as new key:value pair.

# # print(dict1)

# # dict1['state'] = "AndhraPradesh" # If the key is already present inside the dictionary, Previous key value will be updated with new value.

# # print(dict1)


# # Dictionary Keys are unique..

# dict1 = {"name":"ramesh","email":"ramesh@gmail.com","mobile":8284928926,"state":"Telangana","mobile":329320920983}

# # If we have repetition of same key in the dictionary, it will consider the latest key:value pair inside the dictionary..
# # print(dict1)


# # print("mobile" in dict1)

# # if 'city' in dict1: # This is for checking whwther the key is already existed in the dictionary.
# #     pass
# # else:
# #     city = input("Enter your city")
# #     dict1['city'] = city

# # print(dict1)

# # print(dict1['city'])


# # print(dir(dict))

# # nested_dict = {"states":{"state1":"Andhrapradesh","state2":"Telangana"}}

# # print(nested_dict['states']['state2'])

# # Dictionary Methods:

#     # update - Its for adding key:value pairs of 1 dictionary to other dictionary..

# dict1 = {"name":"ramesh","email":"ramesh@gmail.com","mobile":8284928926,"state":"Telangana","mobile":329320920983}


# dict1['city'] = "hyderabad"

# print(dict1)
# dict2 = {'city':"Vizag","Iplteam":"CSK","Captain":"MSDhoni"}

# dict1.update(dict2)

# print(dict1)


#  # removal methods:
#     # pop
#     # popitem
#     # clear

# # pop() - -It will take the key you want to remove and remove the key:value from the dicitonary and will return value as the return output.

# # print(dict1.pop('Iplteam'))

# # popitem() -- It will remove the last key:value pair from the dictionary..


# # print(dict1.popitem())

# # clear() -- It will remove all the key:value pairs and make it as empty dictionary..

# # dict1.clear()

# # print(dict1)


# # Accessing Methods:

# # get() - Its for accessing the respective key:value pair from the dictionary..

# # print(dict1['state'])

# # print(dict1.get('state'))


# # print(dict1['country'])

# # print(dict1.get('country'))


# # print(dict1.get('country','India'))

# # keys() -- It will return all the keys from the dictionary..

# # print(dict1.keys())

# # values() -- It will return all the values from the dictionary..

# # print(dict1.values())

# # items() -- It will return the combination of key and value pair as a list where each key:value pari is taken as tuple..

# # print(dict1.items())

# # copy() - Taking the copy of the first dicionary and creating the new dictionary which same copy..


# # dict2 = dict1.copy()

# # dict2 = dict1

# # print(dict2)

# # dict2['country'] = "India"

# # print(dict1)
# # print(dict2)

# # fromkeys() -- It for converting the list of element into the key:value pair inside the dictionary..

# # list1 = ['state','country',1,'city','course']

# # print({}.fromkeys(list1))

# # print({}.fromkeys(list1,'default'))


# # Iteration :

# dict1 = {'name': 'ramesh', 'email': 'ramesh@gmail.com', 'mobile': 329320920983, 'state': 'Telangana', 'city': 'Vizag', 'Iplteam': 'CSK', 'Captain': 'MSDhoni'}



# key_list = ['city','state','Captain']

# # dict2 = {}

# dict2 = {}.fromkeys(key_list)
# print(dict2)
# for ele in dict1:
#     if ele in key_list:
#         dict2[ele] = dict1[ele]
    

# print(dict2)

# dict3 = {}
# for key,value in dict1.items():
#     print(key,value)
#     if key in key_list:
#         dict3[key] = value

# print(dict3)