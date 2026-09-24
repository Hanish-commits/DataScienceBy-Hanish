# ============================================
# For Loops
# ============================================

# Basic for loop

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# Looping through a string

word = "Python"

for character in word:
    print(character)


# Looping through a list

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# Doing something with each item

numbers = [1, 2, 3, 4]

for number in numbers:
    print(number * 2)


# range()

for number in range(5):
    print(number)


# range(start, stop)

for number in range(1, 6):
    print(number)


# range(start, stop, step)

for number in range(1, 11, 2):
    print(number)


# Counting backwards

for number in range(5, 0, -1):
    print(number)


# Repeating without using the loop variable

for _ in range(3):
    print("Hello Python")


# Tuple

numbers = (10, 20, 30)

for number in numbers:
    print(number)


# Set

fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)


# Dictionary keys

student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

for key in student:
    print(key)


# Dictionary values

for value in student.values():
    print(value)


# Dictionary keys and values

for key, value in student.items():
    print(key, value)


# for loop with if

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(number)


# Accumulating a result

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total = total + number

print(total)


# Nested for loops

for row in range(3):
    for column in range(3):
        print(row, column)


# for loop with else

for number in range(3):
    print(number)
else:
    print("Loop completed")


# Practical example: filter marks

marks = [72, 85, 64, 91, 78]

for mark in marks:
    if mark > 80:
        print(mark)


# Practical example: process names

names = ["hanish", "rahul", "priya"]

for name in names:
    print(name.title())