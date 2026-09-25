# ============================================
# Tuples
# ============================================

# Creating a tuple

fruits = ("apple", "banana", "mango")

print(fruits)
print(type(fruits))


# Empty tuple

items = ()

print(items)


# Tuple without explicit parentheses

numbers = 10, 20, 30

print(numbers)
print(type(numbers))


# Single-item tuple

number = (10,)

print(number)
print(type(number))


# Different data types

student = ("Hanish", 30, 5.9, True)

print(student)


# Tuple indexing

print(fruits[0])
print(fruits[1])
print(fruits[2])


# Negative indexing

print(fruits[-1])
print(fruits[-2])


# Tuple slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[0:3])
print(numbers[2:])
print(numbers[::-1])


# Tuples are immutable

# This produces a TypeError:
# fruits[1] = "orange"


# Tuple length

print(len(numbers))


# Checking whether an item exists

print("banana" in fruits)
print("orange" in fruits)
print("orange" not in fruits)


# count()

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))


# index()

fruits = ("apple", "banana", "mango")

print(fruits.index("banana"))


# Tuple packing

student = ("Hanish", 30, "Data Science")

print(student)


# Tuple unpacking

name, age, course = student

print(name)
print(age)
print(course)


# List to tuple

fruits_list = ["apple", "banana", "mango"]

fruits_tuple = tuple(fruits_list)

print(fruits_tuple)
print(type(fruits_tuple))


# Tuple to list

fruits = ("apple", "banana", "mango")

fruits_list = list(fruits)

print(fruits_list)
print(type(fruits_list))


# Example of fixed data

coordinates = (12.9716, 77.5946)

print(coordinates)