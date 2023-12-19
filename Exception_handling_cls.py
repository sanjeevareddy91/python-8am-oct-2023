# Exception: Error 

# Exception Handlings : Handlings the errors..

list1 = [21,5.6,'python',43,0,12]

# for ele in list1:
#     print(1/ele)

# 2 Types of Exception:
    # Inbuilt Exceptions
    # Userdefined Exceptions

# Syntax:

"""
try:
    statements(Those line of code which might give the error)
except:
    statements(Those lines which i have to execute when ever an error is occured..)
"""

list1 = [21,5.6,'python',43,0,12]

# for ele in list1:
#     try:
#         print(1/ele)
#     except:
#         print('Error occured!')

import sys

# for ele in list1:
#     try:
#         print(1/ele)
#     except:
#         print(sys.exc_info()[0])


# for ele in list1:
#     try:
#         print(1/ele)
#     except TypeError:
#         print("Invalid Type of data,Please provide correct type of data")
#     except ZeroDivisionError:
#         print("Division with 0 not possible in programming")
#     except:
#         print("Error Occured")
    
# Userdefined Exceptions:

# class ValueSmallError(Exception):
#     pass

# class ValuelLargeError(Exception):
#     pass
# import random
# num1 = random.randint(100,500)

# while True:
#     num2 = int(input("Enter your number:"))
#     try:
#         if num2 > num1:
#             raise ValuelLargeError
#         elif num2 < num1:
#             raise ValueSmallError
#         else:
#             print("number guessed!")
#             break
#     except ValueSmallError:
#         print("Value entered is smaller, Try with larger value.")
#     except ValuelLargeError:
#         print("Value entered is larger, Try with smaller value.")


