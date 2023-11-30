# module : Every Python file is going to be called as module..

# import -- Its the keyword for loading the module..

# 1st Syntax:
    # import module-name

# 2nd Syntax:
    # from module-name import functionalities

# import module1  # loading the complete module

# print(module1.name)

# print(module1.add(3,4))

# from module1 import * ## Going inside the module and loading the functionalities

# print(name)
# print(add(3,4))

# from module1 import name,add

# print(name)
# print(add(3,4))



# from module1 import *

# from module2 import *

# print(name)
# print(email)

# print(sub(4,5,6))

# print(add(3,4))


# 1st Syntaxx - Directly laoding the complete module..

# import module1
# import module2


# print(module1.sub(4,5,6))

# print(module1.add(3,4))

# print(module2.add(3,4,5))


# 2nd Syntax: Loading only the functionalities what we require by renaming the function-name..

# from module1 import add
# from module2 import add as module2_add


# print(add(3,4))
# print(module2_add(3,4,5))


# Modules are divided into 3 types:
    # Userdefined Modules -- Those modules(python files) which we create..
    # Inbuilt Modules -- Those which comes defaultly with python installation..
    # External Modules. -- Those which we download based on the requirement..


# Python check into 3 Path when we import a module..
    # 1) Current Working Directory..
    # 2) Where Python is installed..
    # 3) Where we set the environment path..

# import sys

# print(sys.path)

# sys.path.append('C:/Users/reddy/OneDrive/Documents')

# print(sys.path)
# import module2


