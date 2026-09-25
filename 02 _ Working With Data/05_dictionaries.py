# ============================================
# Dictionaries
# ============================================

# Creating a dictionary

student = {
    "name": "Hanish",
    "age": 30,
    "course": "Data Science"
}

print(student)
print(type(student))


# Empty dictionary

empty = {}

print(empty)
print(type(empty))


# Accessing values

print(student["name"])
print(student["age"])


# Using get()

print(student.get("name"))
print(student.get("city"))
print(student.get("city", "Not available"))


# Adding a new key-value pair

student["city"] = "Bengaluru"

print(student)


# Updating a value

student["age"] = 31

print(student)


# pop()

removed = student.pop("age")

print(removed)
print(student)


# popitem()

removed = student.popitem()

print(removed)
print(student)


# del

student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

del student["age"]

print(student)


# clear()

student.clear()

print(student)


# Checking whether a key exists

student = {
    "name": "Hanish",
    "age": 30
}

print("name" in student)
print("city" in student)
print("Hanish" in student)


# keys()

print(student.keys())
print(list(student.keys()))


# values()

print(student.values())
print(list(student.values()))


# items()

print(student.items())


# update()

student.update({
    "age": 31,
    "city": "Bengaluru"
})

print(student)


# Duplicate keys

example = {
    "name": "Hanish",
    "name": "Rahul"
}

print(example)


# Duplicate values

students = {
    "student_1": "Python",
    "student_2": "Python",
    "student_3": "SQL"
}

print(students)


# Different data types as values

student = {
    "name": "Hanish",
    "age": 30,
    "height": 5.9,
    "is_learning": True
}

print(student)


# List inside a dictionary

student = {
    "name": "Hanish",
    "skills": ["Python", "SQL", "Excel"]
}

print(student["skills"])
print(student["skills"][0])


# Dictionary inside a dictionary

student = {
    "name": "Hanish",
    "details": {
        "age": 30,
        "city": "Bengaluru"
    }
}

print(student["details"]["city"])


# Dictionary length

print(len(student))


# Practical example

product = {
    "name": "Laptop",
    "price": 75000,
    "quantity": 2
}

total = product["price"] * product["quantity"]

print(total)