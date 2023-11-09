# lists : Sequence of multiple values seperated with comma(,) declared inside [ ]..

# list1 = [62,5.6,'Python','Django',87]


# print(list1)

# print(type(list1)) # will return the type as list..

# Nested List : Declaring the list inside other list..

# list1 = [32,'python',['Mahesh','Suresh','Subash'],73,'django',32,'datascience']


# Accessing the elements inside the list is done using --- indexing..

# Indexing will start from 0 and will go depending on the length..

# print(list1[0])

# print(list1[2])


# print(list1[1:5]) # ['python', ['Mahesh', 'Suresh', 'Subash'], 73, 'django']

# print(list1[1::2]) # slicing..


# Negative indexing will start from -1.

# print(list1[-1])



# list1 = [32,'python',['Mahesh','Suresh','Subash'],73,'django',32,'datascience']


# print(list1[2:6]) # []


# print(list1[-1:-6:-1])

# Nested Indexing :  Performing the indexing on other indexing outputs..

# print(list1[2][1])

# print(list1[2][1][3])

# print(list1[2][-1::-1])

# print(list1[2][::-1])

# print(len(list1[2]))

# print(len(list1))


# Lists is mutuable...


# list1 = [32,'python',['Mahesh','Suresh','Subash'],73,'django',32,'datascience']
# print(list1)

# list1[1] = 'devops'

# print(list1)

# list1[2] = 'Chennai'

# print(list1) # []

# list1[1:4] = [11,12,13,14,15,16] # this will add the element of the list as seperate value

# print(list1)

# list1[1] = [21,22,23,24] # Here it will add it as single nested as we specified single index value..

# print(list1)

# del list1[1]

# print(list1)

# del list1[1:4]

# print(list1)


# Concatenation(+): Adding of 2 list elements and making it as a single list..
# Repetition(*) : Repeating the elements of a list multiple no.of time..

# print([1,2,3,4]+['python',32,'django'])

# print([2,3,4,5]*3)

# List Methods:

# print(dir(list))

# Adding methods:
    # append
    # extend
    # insert

# removal Methods:
    # remove
    # pop
    # clear

# accessing methods:
    # index
    # count

# alter methods:
    # sort
    # reverse
    # copy


# append -- Its for adding a single element into the list at a time, element will be added to the last index..


list1 = [32,'python',['Mahesh','Suresh','Subash'],73,'django',32,'datascience']

# print(list1)

# list1.append(76)

# print(list1)

# list1.append('datascience')

# print(list1)

# list1.append([31,32,33])

# print(list1)

# Extend -- Its for adding multiple elements into the list at a time and will take only sequence as the element..
    # It wont accept numbers and dictionaries as value inside the extend method..


# list1.extend(43) -- Because integer is not an iterable..

# list1.extend('datascience')

# print(list1)

# list1.extend(['datascience','devops',65])

# print(list1)


# # insert -- It also for adding an single element into the list at a specific index value..

# list1.insert(4,'machinelearning')

# print(list1)

# [(1,2),(4,"django"),(8,"Python")]

# Removal Methods:

# remove -- Its for removing the element from the list, by specifying the element..


list1 = [32,'python',['Mahesh','Suresh','Subash'],73,'django',32,'datascience']
# print(list1)
# # print('ramesh' in list1)

# print(list1.remove('django'))

# print(list1)

# if 'ramesh' in list1:
#     list1.remove('ramesh')

# print(list1)


# # pop -- Its for removing the element from the list,but based on the index value...

# print(list1.pop(4))

# print(list1)


# # clear() -- It will remove all the elements from the list and make it as empty list..

# list1.clear()

# print(list1)


# Accessing methods:
    # index - It will return the index value of an element inside the list..


# print(list1.index('django'))

# # count - How many times a particular element is repeated inside the list..

# print(list1.count(32))


# Altering methods:
    # sort() -- Its for converting the list into ascending or descending order..
        # We have to make sure that all the element inside the list should be of same datatype only.
        # if it contans different datatype it will throw the error.

        # By default sorting is going to perform ascending order..


# list1 = [32,'python',['Suresh','Mahesh','Subash'],73,'django',32,'datascience']

# print(list1)

# list1[2].sort()

# # list1[2]

# print(list1)

list1 = ['Balayya','Chiranjeevi',"Mahesh","Pawankalyan","NTR","Ramcharan","Prabhas","Alluarjun"]

# print(list1)

# # list1.sort()

# # print(list1)

# list1.sort(reverse=True)

# print(list1)


# reverse() -- Reverse the element of the list ...

# list1.reverse()

# print(list1)


list1 = ['Balayya','Chiranjeevi',"Mahesh","Pawankalyan","NTR","Ramcharan","Prabhas","Alluarjun"]


# list2 = list1 # This will assign the memory allocation of list1 to list2..

# list2 = ['Balayya','Chiranjeevi',"Mahesh","Pawankalyan","NTR","Ramcharan","Prabhas","Alluarjun"]

# list2 = list1.copy() # This will copy the values of list1 and create a new memory for the copy and will assign it to the list2..

# print(list1)
# print(list2)

# list1.append(43)

# print(list1)
# print(list2)

# satisified_data = []
# for ele in list1:
#     if ele == 'Balayya':
#         satisified_data.append("Dabidi debidaaaaa")
#     elif ele == "Chiranjeevi":
#         satisified_data.append("Veera shankar Reddddddyyyyyy")
#     elif ele == "Mahesh":
#         satisified_data.append("Kal aag hi meelanga , Party karenga oorrrr janda pathengaaaa")
#     else:
#         print("Not found")

# print(satisified_data)

marks = [64,84,53,94,43,73,63,84,68,53,58]
# print(marks)

# updated_marks = []
# for ele in marks:
#     if ele <90:
#         updated_marks.append(ele+5)

# print(updated_marks)


# updated_marks = []
# for ele in marks:
#     if ele <90:
#         updated_marks.append(ele+5)

#     else:
#         updated_marks.append(ele)

# print(updated_marks)


# List Comprehension : Most Elegnat way of creating the list.

# Syntax1 :

# [expression for ele in sequence]

# Manual Way
# updated_marks = []
# for ele in marks:
#     updated_marks.append(ele+5)

# print(updated_marks)

# # List Comprehension Way
# print([ele+5 for ele in marks])




# 2nd Syntax:

# [expression for ele in sequence if condition]
# Manual Way:
# updated_marks = []
# for ele in marks:
#     if ele <90:
#         updated_marks.append(ele+5)

# print(updated_marks)

# # List Comprehension Way
# print([ele+5 for ele in marks if ele<90])


# 3rd Syntax:

# [expression1 if condition else expression2 for ele in sequence ]


# updated_marks = []
# for ele in marks:
#     if ele <90:
#         updated_marks.append(ele+5)

#     else:
#         updated_marks.append(ele)

# print(updated_marks)

# print([ele+5 if ele<90 else ele for ele in marks])


