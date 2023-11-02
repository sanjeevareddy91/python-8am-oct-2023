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
str1 = "Python is a programming language."

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

str1 = "Python is a programming language."


# str1[0] = 'p' # will throw the error as strings are immutable..


# concatenation(+) - Adding of 2 or more strings and making it as single string..
# Repetition(*). -- Repeating the same string multiple number of times.


hero = "Balayya"

slogan = " Jai Balayya"

# print(hero + slogan)

print(slogan*5)


# dir -- WIll list what are all the methods that i can perform on the value..

print(dir(str))


# Multiline comments
"""
sakjsjkajksa
sasjakjsakjsajk
hsjhasaa
"""