# ============================================
# Parameters & Arguments
# ============================================


# One parameter

def greet(name):
    print(f"Hello {name}")


greet("Hanish")
greet("Rahul")
greet("Priya")


# One parameter with a calculation

def square(number):
    print(number * number)


square(5)
square(10)
square(3)


# Multiple parameters

def add(a, b):
    print(a + b)


add(10, 5)


# Positional arguments

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Hanish", 30)


# Keyword arguments

introduce(age=30, name="Hanish")


# Default parameter

def greet_guest(name="Guest"):
    print(f"Hello {name}")


greet_guest()
greet_guest("Hanish")


# Multiple default parameters

def show_location(name="Guest", city="Unknown"):
    print(f"{name} lives in {city}")


show_location()
show_location("Hanish")
show_location("Hanish", "Bengaluru")


# Required parameter with default parameter

def welcome(name, message="Welcome"):
    print(f"{message}, {name}")


welcome("Hanish")
welcome("Rahul", "Good morning")


# Different data types

def show_value(value):
    print(value)
    print(type(value))


show_value(10)
show_value("Python")
show_value(5.9)
show_value(True)


# Passing a list

def show_fruits(fruits):
    print(fruits)


my_fruits = ["apple", "banana", "mango"]

show_fruits(my_fruits)


# Function with a condition

def check_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


check_even(10)
check_even(7)


# Multiple parameters

def show_profile(name, age, city, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Course: {course}")


show_profile(
    "Hanish",
    30,
    "Bengaluru",
    "Data Science"
)


# Practical calculation

def calculate_total(price, quantity):
    total = price * quantity
    print(f"Total: ₹{total}")


calculate_total(500, 3)
calculate_total(120, 5)


# Practical age check

def check_age(age):
    if age >= 18:
        print("Eligible")
    else:
        print("Not eligible")


check_age(25)
check_age(15)


# Argument can be an expression

square(5 + 2)


# Input + function

def greet_user(name):
    print(f"Hello {name}")


user_name = input("Enter your name: ")

greet_user(user_name)