# ============================================
# Scope
# ============================================


# Local scope

def greet():
    name = "Hanish"
    print(name)


greet()


# This would cause a NameError because name
# exists only inside the function.
#
# print(name)


# Global scope

name = "Hanish"


def show_name():
    print(name)


show_name()


# Local and global variables with the same name

name = "Global Hanish"


def show_local_name():
    name = "Local Hanish"
    print(name)


show_local_name()
print(name)


# Global variable and local assignment

count = 10


def update_count():
    count = 20
    print(count)


update_count()

print(count)


# Using global

count = 10


def update_global_count():
    global count
    count = 20


update_global_count()

print(count)


# Parameters have local scope

def greet_user(name):
    print(name)


greet_user("Hanish")

# print(name)  # NameError


# return and scope

def get_name():
    name = "Hanish"
    return name


result = get_name()

print(result)


# Different functions can have local
# variables with the same name

def first():
    value = 10
    print(value)


def second():
    value = 20
    print(value)


first()
second()


# Nested functions

def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()


outer()


# LEGB example

value = "global"


def outer_function():
    value = "enclosing"

    def inner_function():
        value = "local"
        print(value)

    inner_function()


outer_function()


# Built-in scope

numbers = [10, 20, 30]

print(len(numbers))
print(type(numbers))


# Avoid shadowing built-ins

# This is a bad idea:
#
# print = "Hello"
#
# It can interfere with the built-in print() function.


# Practical example

price = 500


def calculate_total(quantity):
    total = price * quantity
    return total


result = calculate_total(3)

print(result)


# Better: use parameters

def calculate(price, quantity):
    return price * quantity


result = calculate(500, 3)

print(result)


# Scope with a loop

for number in range(3):
    print(number)

print(number)