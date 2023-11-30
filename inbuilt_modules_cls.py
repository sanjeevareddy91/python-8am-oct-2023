# # Inbuilt Modules - Those modules which comes defaultly with python installation..

# # print(help('modules'))

# # random
# # datetime
# # os
# # json
# # csv
# # dateutil
# # tkinter

# # import random 

# # print(dir(random))
#     # randint  
#     # randrange
#     # choice
#     # choices

# import random

# # print(random.randint(1000,10000))

# # print(random.randint(100000,1000000))

# # print(random.randrange(100000,1000000))

# # print(random.randrange(10,35,3)) # 10,13,16,19,22,25,28,31,34


# a=['SWIGGYIT','SWIGGY50','SWIGGY40','SWIGGYBIRTHDAY']

# # print(random.choice(a))

# lotteries = ['LOT1','LOT2','LOT15','LOT16','LOT71','LOT738','LOT634','LOT43']

# # print(random.choices(lotteries,k=3))


# # datetime -- 

# # import datetime

# from datetime import datetime

# # print(dir(datetime))

# # print(datetime.now())

# # print(datetime.today())

# # print(datetime.now().date().year)

# # print(datetime.now().time().minute)


# from datetime import timedelta

# # subscription_date = datetime.now()

# # print(subscription_date)

# # subscription_end_date = subscription_date+timedelta(days=30)

# # print(subscription_end_date)

# # session_started = datetime.now()
# # print(session_started)

# # session_ended = session_started+timedelta(minutes=10)

# # print(session_ended)

# from dateutil.relativedelta import relativedelta

# # print(datetime.now()+timedelta(days=90))

# # print(datetime.now()+relativedelta(months=3))

# # print(datetime.now()+timedelta(days=-90))



# # before_1 = datetime.now() - relativedelta(months=1)

# # print(before_1)

# # print(before_1+timedelta(days=90))

# # print(type(before_1+relativedelta(months=3)))


# # strftime -- This is for converting python datetime to string..
# # strptime

# today_date = datetime.now()

# print(today_date)

# # print(type(today_date))

# # # print(today_date.strftime('%Y-%m-%d %H:%M:%S'))

# # # print(type(today_date.strftime('%Y-%m-%d')))

# # print(today_date.strftime('%d-%m-%Y %H:%M:%S %p %A %B'))
# # time_after = datetime.now()+timedelta(hours=6)
# # # print(today_date.strftime('%d-%m-%Y %I:%M:%S %A %B'))

# # print(time_after)
# # print(time_after.strftime('%d-%m-%Y %I:%M:%S %p %A %B'))


# # strptime() -- String to python datetime..

# # str_date = '23 April 2021 04:15 PM'

# # print(str_date)

# # print(type(str_date))
# # converted_date = datetime.strptime(str_date,'%d %B %Y %I:%M %p')

# # print(converted_date)

# # print(type(converted_date))


# str_date = '23April2021 04:15 PM'

# print(str_date)

# print(type(str_date))
# converted_date = datetime.strptime(str_date,'%d%B%Y %I:%M %p')

# print(converted_date)

# print(type(converted_date))

import os
# print(dir(os))

# getcwd()
# listdir()
# mkdir()
# makedirs
# rmdir()
# removedirs()
# remove
# rename
# open()
# environ()

# print(os.getcwd()) # Current Woking Directory.

os.chdir('C:/Users/reddy')

# print(os.getcwd()) # Current Woking Directory.

# print(os.listdir('.')) # This will return all the folders and files from the current working directory..

# print(os.listdir('C:/Users/reddy/OneDrive/Desktop')) # This will return all the folders and files from the specified directory..

# os.mkdir('Python-check') # This will create a folder with the specified name in the current working directory..

# os.makedirs('Django/Fodler1/Folder2')

# os.removedirs('Django/Fodler1/Folder2')

# os.rmdir()

# os.remove('C:/Users/reddy/OneDrive/Documents/module2_cls.py')

# print(list(os.walk('C:/Users/reddy/OneDrive/Documents/Django-8am')))

# External Modules...

# pip -- python package manager

# pip install package-name 

# pymysql
# MySQLdb
# psycopg2
# python-facebook-api

# pip uninstall package-name

# pip list or pip freeze -- for listing all the libraries which are installed externally..

# boto3 -- 
# pandas -- 