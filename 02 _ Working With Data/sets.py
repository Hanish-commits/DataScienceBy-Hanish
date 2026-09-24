# ============================================
# Sets
# ============================================

# Creating a set

fruits = {"apple", "banana", "mango"}

print(fruits)
print(type(fruits))


# Duplicate values are automatically removed

numbers = {10, 20, 20, 30, 30}

print(numbers)


# Empty dictionary vs empty set

empty_dictionary = {}

print(type(empty_dictionary))

empty_set = set()

print(type(empty_set))


# Set length

print(len(numbers))


# Checking membership

print("banana" in fruits)
print("orange" in fruits)
print("orange" not in fruits)


# add()

fruits.add("orange")

print(fruits)

fruits.add("apple")

print(fruits)


# update()

fruits.update(["grape", "watermelon"])

print(fruits)


# remove()

fruits.remove("banana")

print(fruits)


# discard()

fruits.discard("pineapple")

print(fruits)


# pop()

removed_item = fruits.pop()

print(removed_item)
print(fruits)


# clear()

numbers = {10, 20, 30}

numbers.clear()

print(numbers)


# --------------------------------------------
# Set Operations
# --------------------------------------------

python_students = {"A", "B", "C", "D"}
sql_students = {"C", "D", "E", "F"}


# Union

all_students = python_students | sql_students

print(all_students)

all_students = python_students.union(sql_students)

print(all_students)


# Intersection

both = python_students & sql_students

print(both)

both = python_students.intersection(sql_students)

print(both)


# Difference

only_python = python_students - sql_students

print(only_python)

only_sql = sql_students - python_students

print(only_sql)


# Symmetric difference

different = python_students ^ sql_students

print(different)

different = python_students.symmetric_difference(sql_students)

print(different)


# --------------------------------------------
# Set Comparisons
# --------------------------------------------

numbers = {1, 2, 3, 4, 5}
small_numbers = {1, 2, 3}


# Subset

print(small_numbers.issubset(numbers))


# Superset

print(numbers.issuperset(small_numbers))


# Disjoint sets

set_a = {1, 2, 3}
set_b = {4, 5, 6}

print(set_a.isdisjoint(set_b))


# --------------------------------------------
# Removing duplicates from a list
# --------------------------------------------

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)

unique_numbers = list(set(numbers))

print(unique_numbers)


# --------------------------------------------
# Practical example
# --------------------------------------------

class_a = {"Hanish", "Rahul", "Aman", "Priya"}
class_b = {"Priya", "Aman", "Riya", "Karan"}

all_students = class_a | class_b
both_classes = class_a & class_b
only_a = class_a - class_b

print(all_students)
print(both_classes)
print(only_a)