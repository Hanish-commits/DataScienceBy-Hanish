# ============================================
# Strings
# ============================================

# Creating strings

name = "Hanish"
city = 'Bengaluru'

print(name)
print(city)
print(type(name))


# Multiline string

message = """Python is interesting.
I am learning it step by step.
Practice is helping me understand it."""

print(message)


# String length

word = "Python"

print(len(word))

message = "Hello Python"

print(len(message))


# String indexing

word = "Python"

print(word[0])
print(word[1])
print(word[5])


# Negative indexing

print(word[-1])
print(word[-2])


# String slicing

print(word[0:3])
print(word[:3])
print(word[3:])
print(word[1:5])


# Slicing with a step

print(word[::2])


# Reversing a string

print(word[::-1])


# Strings are immutable

word = "Python"

# word[0] = "J"   # TypeError

word = "J" + word[1:]

print(word)


# String concatenation

first_name = "Hanish"
last_name = "Sharma"

full_name = first_name + " " + last_name

print(full_name)


# String repetition

greeting = "Hi "

print(greeting * 3)


# Checking whether text exists

message = "Python is fun"

print("Python" in message)
print("Java" in message)
print("Java" not in message)


# String methods

text = "Python Is FUN"

print(text.lower())
print(text.upper())


# strip()

text = "   Python   "

print(text.strip())


# replace()

text = "I am learning Java"

text = text.replace("Java", "Python")

print(text)


# find()

text = "Python is powerful"

print(text.find("powerful"))
print(text.find("Java"))


# count()

text = "python is fun and python is powerful"

print(text.count("python"))


# startswith()

text = "Python programming"

print(text.startswith("Python"))


# endswith()

file_name = "data.csv"

print(file_name.endswith(".csv"))


# split()

sentence = "Python is easy to learn"

words = sentence.split()

print(words)


# join()

words = ["Python", "is", "fun"]

sentence = " ".join(words)

print(sentence)


# Character checking methods

text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())


# Escape characters

print("Hello\nPython")
print("Python\tData Science")


# f-string

name = "Hanish"
course = "Data Science"

print(f"My name is {name} and I am learning {course}.")


# Small practical example

user_name = input("Enter your name: ")

user_name = user_name.strip()
user_name = user_name.title()

print(f"Hello, {user_name}!")