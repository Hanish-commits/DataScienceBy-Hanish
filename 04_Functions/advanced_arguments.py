# ============================================
# Advanced Function Arguments
# ============================================


# --------------------------------------------
# *args
# --------------------------------------------

def show_numbers(*args):
    print(args)


show_numbers(10, 20)
show_numbers(10, 20, 30)
show_numbers(10, 20, 30, 40, 50)


# *args is a tuple

def check_args(*args):
    print(args)
    print(type(args))


check_args(10, 20, 30)


# Working with args

def show_values(*args):
    print(len(args))
    print(args[0])
    print(args[-1])


show_values(10, 20, 30, 40)


# Looping through args

def print_numbers(*args):
    for number in args:
        print(number)


print_numbers(10, 20, 30)


# Practical example: total

def calculate_total(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(calculate_total(10, 20))
print(calculate_total(10, 20, 30))
print(calculate_total(10, 20, 30, 40, 50))


# Different data types

def show_values(*args):
    print(args)


show_values("Python", 10, True, 5.9)


# --------------------------------------------
# **kwargs
# --------------------------------------------

def show_profile(**kwargs):
    print(kwargs)


show_profile(
    name="Hanish",
    age=30,
    city="Bengaluru"
)


# Accessing kwargs values

def print_profile(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])
    print(kwargs["city"])


print_profile(
    name="Hanish",
    age=30,
    city="Bengaluru"
)


# Looping through kwargs

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


show_details(
    name="Hanish",
    age=30,
    city="Bengaluru"
)


# **kwargs is a dictionary

def check_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))


check_kwargs(
    name="Hanish",
    age=30
)


# --------------------------------------------
# Combining normal parameters with *args
# --------------------------------------------

def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}")


greet("Hello", "Hanish", "Rahul", "Priya")


# --------------------------------------------
# Combining normal parameters with **kwargs
# --------------------------------------------

def show_course(course, **details):
    print(f"Course: {course}")
    print(details)


show_course(
    "Data Science",
    duration="12 months",
    mode="Online"
)


# --------------------------------------------
# Combining normal parameters, *args and
# **kwargs
# --------------------------------------------

def profile(name, *skills, **details):
    print(name)
    print(skills)
    print(details)


profile(
    "Hanish",
    "Python",
    "SQL",
    city="Bengaluru",
    goal="Data Science"
)


# --------------------------------------------
# Keyword-only arguments
# --------------------------------------------

def create_profile(name, *, age, city):
    print(name, age, city)


create_profile(
    "Hanish",
    age=30,
    city="Bengaluru"
)


# --------------------------------------------
# Positional-only arguments
# --------------------------------------------

def calculate(a, b, /):
    return a + b


print(calculate(10, 20))

# This is not allowed:
# calculate(a=10, b=20)


# --------------------------------------------
# Positional argument unpacking
# --------------------------------------------

numbers = [10, 20, 30]


def add(a, b, c):
    return a + b + c


result = add(*numbers)

print(result)


# --------------------------------------------
# Dictionary unpacking
# --------------------------------------------

details = {
    "name": "Hanish",
    "age": 30
}


def show_profile(name, age):
    print(name, age)


show_profile(**details)


# --------------------------------------------
# Practical dictionary example
# --------------------------------------------

product = {
    "name": "Laptop",
    "price": 75000,
    "quantity": 2
}


def show_product(name, price, quantity):
    print(f"Product: {name}")
    print(f"Price: ₹{price}")
    print(f"Quantity: {quantity}")


show_product(**product)