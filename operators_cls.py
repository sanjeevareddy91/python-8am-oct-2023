# operator : A symbol which performs the operation between operands..

# Arthimetic Operators(+,-,*,/,//,%,**)
# Relational or Comparison Operators(==,!=,>,<,>=,<=)
# Logical Operators(and,or,not)
# Assignment Operators(=,+=,-=,*=......)
# Membership Operators(in,not in)
# Identity Operators(is, is not)
# Bitwise Operators(Bitwise AND(&),Bitwise OR(|),Bitwise XOR(^),Left shift(<<),Right Shift(>>),Bitwise NOT(~))
# Ternary Operator()


# Arthimetic Operators:

# /                //            %


# 17/3 - 5.6666667                   17//3 -5                         17%3 - 2

# 3)17(5.6666667                    3) 17 (5.66667                    3)17(5
#   15                                 15                               15
# -------                           ------------                      --------
#    20                                20                                2
#    18                                18
# ------                            ------------
#     2                                 2


# 3)167(55
#   15
# ---------
#    17
#    15
# ---------
#     2


# ** -- power

# print(3*4)

# print(3**4)


# Relational Operators()


# name = "Kishore" # THis will assign the value to name varibale..


# # print(name == 'kishore')  # We are checking whether name value and "kishore" is same or not

# # print(name != 'kishore')

# # a=21

# # print(a>30)

# print(name > 'kishore') # False..


# Logical Operators(and,or,not):


# BODMAS - 
# A        B        A and B       A or B         not(A)      not(A and B)      not((A or B) and (A and B))
# -----------------------------------------------------------------------------------------------------------
# T        F           F            T              F                T                      T 
# F        T           F            T              T                T                      T 
# T        T           T            T              F                F                      F 
# F        F           F            F              T                T                      T 

# username = "rajesh"
# password = "password"

# input() -- It will help you to gve the userinput at runtime..

# username1 = input("Enter your username:")

# password1 = input("Enter your password:")


# mobile = "8898398876"

# # print(username1 == username and password1==password)

# mobile1 = input("Enter your number:")

# # print((username1 == username and password1==password) or (mobile1 == mobile and password1==password))


# print((username1 == username or mobile1==mobile) and (password1==password))

# Assignment Operators(=,+=,-=,/=,*=):

# a=32  

# a+=5 # a=a+5

# print(a)

# a-=2
# print(a)

# a*=3
# print(a)

# Membership Operators(in,not in):

# str1 = "Python is a programming language."

# print('P' in str1)

# print('prog' in str1)

# print('s ap' in str1) # False

# print('s ap' not in str1) # True


list1 = ["7372873287","7382873232","8392893232","93728728732","7382382929","9327328233"]


# print("8392893232" in list1) # True

# print("839289323" in list1) # (False)complete value has to match not the subpart


tuple1 = ("7372873287","7382873232","8392893232","93728728732","7382382929","9327328233")

# print("8392893232" in tuple1) # True

# print("839289323" in tuple1) # (False)complete value has to match not the subpart


# address = {"H.no":301,"building-name":"lake view","Locality":"Madhapur","city":"Hyderabad","pincode":"500084"}


# print('city' in address)

# print('500084' in address)

# Identity Operators(is,is not):

# a=12

# print(a is 12)
# print(a == 12)


# name="ramesh"

# print(name is 'ramesh')
# print(name == 'ramesh')

# tuple1 = (1,2,3,4)

# print(id(tuple1))
# print(tuple1 is (1,2,3,4))

# print(id((1,2,3,4)))

# print(tuple1 == (1,2,3,4))

# list1 = [1,2,3,4]

# print(list1 is [1,2,3,4])  # it will check the memory allocation
# print(list1 == [1,2,3,4])

# print(id(list1))
# print(id([1,2,3,4]))

# print(list1 is not [1,2,3,4])


# Bitwise Operators:(Bitwise AND(&),Bitwise OR(|),Bitwise XOR(^),Bitwise NOT(~),Left Shift(<<),Right Shift(>>))

# A       B     A&B     A|B     A^B 
# -----------------------------------
# 0       1      0       1       1
# 1       0      0       1       1 
# 1       1      1       1       0
# 0       0      0       0       0

a=14

b=23

# print(a&b)
# print(a|b)
# print(a^b)

# a = 14(1110)

# 2)14(
#    2)7 - 0 
#       2) 3 - 1
#          1 - 1

# b=23(10111)

# 2)23(
#    2)11 - 1
#       2) 5 - 1
#          2)2 - 1
#            1 - 0

# print(bin(14))
# print(bin(23))

# 14 - 01110
# 23 - 10111
# -----------
#    - 00110 - &
#    - 11111 - |
#    - 11001 - ^

# print(int('110',2))

# 110


# 1010110 -- 64+0+16+0+4+2+0


# 1010100101
#      1024 512 256 128  64 32  16 8 4 2 1
#               512+128+32+4+1


# print(int('1010100101',2))


# Left Shift(<<):

a=28

# 0001 1100 

# a<<1

# 0001 1100 - bin of 28
# 0011 1000 - Left Shift of 28

# a>>1

# 0000 1110 - right shift of 28

# print(a<<1)
# print(a>>1)

# print(a<<2)
# print(a>>2)


# Bitwise NOT(~)

# a=28

# print(~a)

# # 11100 -- 00011

# 00011
# 11100 - 1's complement of 00011
#     1
# -------------------
# 11101 - 2's complement of 000111

# 011111
#     1
# ---------
# 100000

# a=-56

# print(~a)


