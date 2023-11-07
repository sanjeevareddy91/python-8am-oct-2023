# lists : Sequence of multiple values seperated with comma(,) declared inside [ ]..

list1 = [62,5.6,'Python','Django',87]


print(list1)

print(type(list1)) # will return the type as list..

# Nested List : Declaring the list inside other list..

list1 = [32,'python',['Mahesh','Suresh','Subash'],73,'django',32,'datascience']


# Accessing the elements inside the list is done using --- indexing..

# Indexing will start from 0 and will go depending on the length..

# print(list1[0])

# print(list1[2])


# print(list1[1:5]) # ['python', ['Mahesh', 'Suresh', 'Subash'], 73, 'django']

# print(list1[1::2]) # slicing..


# Negative indexing will start from -1.

# print(list1[-1])



list1 = [32,'python',['Mahesh','Suresh','Subash'],73,'django',32,'datascience']


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