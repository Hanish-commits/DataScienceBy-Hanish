# ============================================
# Lists
# ============================================

# Creating a list

fruits = ["apple", "banana", "mango"]

print(fruits)


# Empty list

items = []

print(items)


# List with different data types

student = ["Hanish", 30, 5.9, True]

print(student)


# List indexing

print(fruits[0])
print(fruits[1])
print(fruits[2])


# Negative indexing

print(fruits[-1])
print(fruits[-2])


# List slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])


# Lists are mutable

fruits[1] = "orange"

print(fruits)


# Length of a list

print(len(fruits))


# append()

fruits.append("banana")

print(fruits)


# insert()

fruits.insert(1, "grape")

print(fruits)


# extend()

fruits.extend(["pineapple", "watermelon"])

print(fruits)


# Difference between append() and extend()

list_one = ["apple", "banana"]

list_one.append(["mango", "orange"])

print(list_one)

list_two = ["apple", "banana"]

list_two.extend(["mango", "orange"])

print(list_two)


# remove()

fruits.remove("banana")

print(fruits)


# pop()

removed_item = fruits.pop(1)

print(removed_item)
print(fruits)


# pop() without an index

removed_item = fruits.pop()

print(removed_item)
print(fruits)


# del

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)


# clear()

numbers.clear()

print(numbers)


# Checking whether an item exists

fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
print("orange" in fruits)
print("orange" not in fruits)


# index()

print(fruits.index("banana"))


# count()

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))


# sort()

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)


# sort() in descending order

numbers.sort(reverse=True)

print(numbers)


# reverse()

fruits = ["apple", "banana", "mango"]

fruits.reverse()

print(fruits)


# copy()

fruits = ["apple", "banana", "mango"]

new_fruits = fruits.copy()

new_fruits.append("orange")

print(fruits)
print(new_fruits)


# Same list reference

original = ["apple", "banana", "mango"]

another = original

another.append("orange")

print(original)
print(another)


# Nested list

numbers = [
    [1, 2, 3],
    [4, 5, 6]
]

print(numbers)
print(numbers[0][1])