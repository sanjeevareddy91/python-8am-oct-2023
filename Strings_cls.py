# Strings : Sequence of anything declared inside " "...


# name = "Suresh"

# print(name)
# print(type(name))

# name = 'Suresh'

# print(name)
# print(type(name))


# name = """Suresh"""
# print(name)
# print(type(name))


# ' ' or " " -- Single line string 

# """ """ or ''' ''' -- Multiline strings.

# poem = 'Twinkle Twinkle little star 
# how i wonder what u r'

# poem1 = "Twinkle Twinkle little star 
# how i wonder what u r"

# print(poem)
# print(poem1)


# poem2 = '''Twinkle Twinkle little star 
# how i wonder what u r'''

# print(poem2)

# poem = 'Twinkle Twinkle' little star '


# poem = 'Twinkle Twinkle" little star '

# print(poem)


# Accessing the elements inside the string.. -- Indexing

# Indexing will start from 0 and will goon depending on the value length..

# [] -- Its the symbol for performing the indexing..

str1 = "Python is a programming language."

# print(str1[0])

# print(str1[14])

# print(str1[7:19]) # last index +1

# slcing -- Performing the jumps or offset..

# print(str1[0:10:1]) # Default value for 3rd argument will be 1..

# print(str1[0:10:2])


# Negative Indexing -- It will start from -1..
# str1 = "Python is a programming language."

# print(str1[-1])

# print(str1[-6])

# print(str1[-2:-9:1]) # This will return the output as empty, as slicing is going to perfrom the operation in positive order but we require it in negative order..

# print(str1[-2:-10:-1])

# print(str1[-1:-(len(str1)+1):-1])

# len -- will return the lenght of the sequence

# print(str1[::-1])

# data = str1[-2:-10:-1]

# print(data[::-1])

# print(str1[24:32])

# str1 = "Python is a programming language."


# print(str1[-9:32])

# print(str1[-9])

# print(str1[-9:])


# Immutable -- Those Which we cannot change once the declartion is done.

# str1 = "Python is a programming language."


# str1[0] = 'p' # will throw the error as strings are immutable..


# concatenation(+) - Adding of 2 or more strings and making it as single string..
# Repetition(*). -- Repeating the same string multiple number of times.


# hero = "Balayya"

# slogan = " Jai Balayya"

# print(hero + slogan)

# print(slogan*5)


# # dir -- WIll list what are all the methods that i can perform on the value..

# print(dir(str))


# # Multiline comments
# """
# sakjsjkajksa
# sasjakjsakjsajk
# hsjhasaa
# """

# print(dir(str))

# startswith,endswith,isalpha,isalnum,isdigit,islower,isupper,lower,upper,title,capitalize,swapcase,index,find,count,replace,split,strip,zfill,join,format.



dialogue = "Dont trouble the trouble if you toruble the truoble trouble troubles you i am not the trouble i am the truth"

#startswith() -- Its just for checking whwther the string is starting with what we specified or not.

#endswith() -- Its just for checking whwther the string is ending with what we specified or not.

# print(dialogue.startswith('D'))

# print(dialogue.startswith("Don't"))

# print(dialogue.endswith('truth'))

# print(dialogue.endswith('Truth'))


# isalpha() - It will check whwther everything inside the string are alphabets only..

# print(dialogue.isalpha())

# email = "gsanjeev@gmail.com"

# print(dialogue.isalpha())


# first_name = "Sanjeev"

# print(first_name.isalpha())


# isalnum() -- It will check whwther everything inside the string are alphanumeric values..


# pancard = "KAG62HTE8y"

# print(pancard.isalnum())

# aadhar = "82982919821912"

# print(aadhar.isalnum())

# Firstname = "Sanjeeva"
# print(Firstname.isalnum())


# pancard = "KAG62 HTE8y"

# print(pancard.isalnum())


# isdigit() - It is to check whether everything inside the string is numbers only..

# mobile = "821929121098"

# print(mobile.isdigit())

# mobile = "8219291 21098"

# print(mobile.isdigit())

# islower() - Its to check whwther everything inside the string is lowercase only..
# isupper() - Its to check whwther everything inside the string is uppercase only..

# sample1 = "PYTHON PROGRAMMING 261721"

# print(sample1.isupper())

# sample1 = "django 261721"

# print(sample1.islower())

# lower() - Its for converting all the alphabets into lower case..

# upper() - Its for converting all the alphabets into upper case..

# email = "GSANjeev123@GMail.com"

# print(email.lower())

# print(email.upper())

# title() -- Each word starting alphabet will be converted into uppercase inside the string..

# dialogue = "Dont trouble the trouble if you tROUBLE the truoble trouble troubles you i am not the trouble i am the truth"

# print(dialogue.title())

# dialogue = "Dont trouble the 6217trouble if @#@#you tROUBLE the truoble trouble troubles you i am not the trouble i am the truth"

# print(dialogue.title())

# # capitalize - Only starting charcater of the string will be converted to uppercase..

# print(dialogue.capitalize())

# # swapcase() -- Converting lowercase to upper and upper to lowercase..

# print(dialogue.swapcase())

# print(dialogue)

# index -- It will return the index value of the element inside the string..

sample1 = "Django2121 is a we21b framework 72for python"

# print(sample1.index('f'))

# print(sample1.index('is'))

# print(sample1.index('b frame'))

# print(sample1.index('72'))

# print(sample1.index('o'))


# count -- It will return how many times a particular elements repeated inside the string..

# print(sample1.count('o'))

# Task:
# str1 = "Djang2121 is a we21b framework 72for python"
# Enter which elements: 'o'
# Input("O has occcured 4 time, which occurece you want..")