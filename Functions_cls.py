# Functions: Set of lines of code which performs a specific task...
    # Write the code once and use it n no.of times..


# a=32
# b=43

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# print("-------------------------------------------")
# a=12
# b=13

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# def --- its the keyword for functions..

"""
def functionname():
    statement
"""
# a=34
# b=43

# def arthimetic():
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)


# # Function call is mandatory...
# arthimetic()

# a=12
# b=13

# arthimetic()


# print(a)
# print(b)


# def arthimetic(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a)
#     print(b)
#     print("-------------------------------")
# arthimetic(34,43)
# # print(a) -- This will throw the error as 'a' is a local varibales isnide the function only..

# arthimetic(12,13)

# arthimetic(13,14)


# Different ways of passing the arguments:
    # 1) Positional Arguments 
    # 2) Default Arguments
    # 3) Keyword Arguments
    # 4) Arbitrary Positional Arguments
    # 5) Arbitrary Keyword Arguments


# Positional Arguments :  Assiging the value to te arguments based on the position of values passed..

# def login(username,password):
#     print(username)
#     print(password)
#     if username == 'ramesh' and password == 'ramesh@123':
#         print("Login Successful!")
#     else:
#         print("Invalid Credentials")


# # login('ramesh','password@123')

# # login('ramesh','ramesh@123')

# login('ramesh@123','ramesh')

# # login('ramesh') # This is an error as it require 2 arguments

# # login('ramesh','ramesh@123','ramesh@gmail.com') # This is an error as it require 2 arguments



# Default Arguments: Passing the default value to an argument at the function declaration..
    # if we pass any value at the function call default value will be overridden..


# def employee_info(emp_id,emp_name,work_location="Bangalore"):
#     print(f"HI {emp_name}, Your employee id is {emp_id} and your work location is {work_location}")

# employee_info(161,'Suresh','Chennai')

# employee_info(183,'Mahesh')

# ******First all the positional argument has to be declared after that default arguments has to be declared..

# def employee_info(emp_id,work_location="Bangalore",emp_name): # This is an Error..
#     print(f"HI {emp_name}, Your employee id is {emp_id} and your work location is {work_location}")


# Keyword Arguments:

    # Passing the value at the function call based on the argument name..

# def employee_info(emp_id,emp_name,work_location):
#     print(f"HI {emp_name}, Your employee id is {emp_id} and your work location is {work_location}")


# employee_info(43,'suresh','Mumbai')
# employee_info(emp_id=43,emp_name='suresh',work_location='Mumbai')


# # employee_info('suresh','Mumbai',43)
# employee_info(emp_name='suresh',work_location='Mumbai',emp_id=43)

# employee_info(43,work_location='Mumbai',emp_name='suresh')

# employee_info(emp_name='suresh',emp_id=43,'Mumbai') # This will throw the error..

# While passing the values first all the positional values should be declared afterthat keyword value should be declared.

# employee_info(43,emp_name='Suresh',emp_id=43,work_location='Chennai') # This is an error.

# 4) Arbitrary Positional Arguments: Passing multiple positional values to the function call..

# * -- Symbol for declaring the multiple positional arguments..


# def cred_trans(*trans):
#     amount = 0
#     for ele in trans:
#         amount+=ele # amount = amount+ele
#     print(f"Hi, You have done {len(trans)} transactions for an amount of {amount}/-")

# cred_trans(4324,5343,5433)

# cred_trans(8755,5353,644,7745)

# cred_trans(7474,674,7484,4644,7758)

# Arbitrary Keyword Arguments: Passing multiple keyword values to the function call..

# ** -- Symbol for declaring the Arbitrary Keyword arguments..

# def cred_trans(**trans):
#     print(trans)
#     amount = 0
#     for ele in trans:
#         amount = amount+trans[ele]
#     print(f"Hi, You have done {len(trans)} transactions for an amount of {amount}/-")

# cred_trans(date_2=6372,date_10=7484,date_18=8373)

# cred_trans(date_2=6372,date_10=7484,date_18=8373,date_12=7848)

# cred_trans(date_2=6372,date_10=7484,date_18=8373,date_13=4847,date_23=894)

# Combination of arbitrayr positional and keyword arguments.

# def cred_trans(*trans,**info):
#     print(trans)
#     print(info)
#     amount = 0
#     for ele in trans:
#         amount = amount+ele
#     print(f"Hi {info['name']},You credit card statement for an amount of {amount}/- has been sent to {info['email']}.")

# cred_trans(5464,7474,7474,name='suresh',email='suresh@gmail.com')

# cred_trans(5464,7474,7474,8484,6474,name='ramesh',email='ramesh@gmail.com')


# Local and Global variables..

# Local varibales : Those varibales which we passed as argument to the function or declred inside the functionand can be accessed only inside the funciton itself.
# Global Variables : Those varibales which we declared outside of the functiona and can be acessed anywhere without restrictions..
# name = "suresh" # global variables

# def info(email,mobile): # local variables
#     # global name
#     global email1
#     email1 = email
#     name = "ramesh"
#     print(f"Hi {name}, your email is {email} and mobile number is {mobile}")

# info("suresh@gmail.com","8998489484")

# print(name)
# print(email1)


# Return statement:



# def add(a,b):
#     print(a+b)
#     return a+b
#     print("hello")

# # # print(add(3,4))

 
# def cal(a,b,c,d):
#     return (add(a,b)-(c-d))

# print(cal(3,4,2,1))

# Recursion : A Function calling itself..


# n! = n*(n-1)!
# 6! = 6*5!
#      6*5*4!
#      6*5*4*3!
#      6*5*4*3*2!
#      6*5*4*3*2*1!
#      6*5*4*3*2*1*1

# def cal_fact(a):
#     if a==1 or a==0:
#         return 1
#     else:
#         return a*cal_fact(a-1) # 6*5*4*3*2*1
    

# print(cal_fact(6))


# Task1:

# dict1 = {
#     'sasa':"SASA",
#     "haja":"HAJA",
#     "gdhr":{
#         "hajs":"HAJS",
#         "ytyr":"YTYR",
#         "khre":{
#             "jtkr":"JTKR",
#             "uthr":"UTHR"
#         },
#         "htkr":"HTKR"
#     },
#     "kyre":"KYRE"
# }

# output

# dict1 = {
#     'SASA':"SASA",
#     "HAJA":"HAJA",
#     "HDGR":{
#         "HAJS":"HAJS",
#         "YTYR":"YTYR",
#         "KHRE":{
#             "JTKR":"JTKR",
#             "UTHR":"UTHR",

#         },
#         "JTKR":"HTKR"
#     },
#     "KYRE":"KYRE"
# }

# Lambda Functions or Anonymous Functions..-- A Function which doesnot have any name...

# lambda arguments:expression


data = lambda a,b:a+b

print(data(2,3))


# map
# filter


a=[35,64,44,22,33,44,99,44,74,65]

# new = []

# def info(a):
#     for ele in a:
#         new.append(ele+2)
# info(a)

# print(new)

# print([ele+2 for ele in a])


# print(list(map(lambda i:i+2,a)))

# a=['73828283738','4994484944','9484847575','6733783933','9484484848','8474744874','9484448484']

# new = []

# def check(a):
#     for ele in a:
#         if ele.startswith('9'):
#             new.append(ele)
# check(a)

# print(new)


# print([ele for ele in a if ele.startswith('9')])

# print(list(map(lambda i:i.startswith('9'),a)))

# print(list(filter(lambda i:i.startswith('9'),a)))