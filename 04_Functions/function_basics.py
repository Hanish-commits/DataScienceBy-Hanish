# ============================================
# Function Basics
# ============================================


# Defining a simple function

def welcome():
    print("Welcome to Python")


# Calling the function

welcome()


# Calling the same function multiple times

welcome()
welcome()


# Simple functions for different tasks

def say_hello():
    print("Hello!")


def show_course():
    print("I am learning Data Science")


say_hello()
show_course()


# A function with multiple statements

def show_profile():
    name = "Hanish"
    age = 30
    course = "Data Science"

    print(name)
    print(age)
    print(course)


show_profile()


# Using a variable defined outside the function

name = "Hanish"


def greet():
    print(name)


greet()


# Function containing a for loop

def print_numbers():
    for number in range(1, 6):
        print(number)


print_numbers()


# Function containing an if statement

def check_age():
    age = 20

    if age >= 18:
        print("Adult")
    else:
        print("Not an adult")


check_age()


# Reusability

def show_message():
    print("Hello Hanish")


show_message()
show_message()
show_message()


# Practical example

def learning_status():
    print("Learning Python")
    print("Building programming foundations")
    print("Working toward Data Science")


learning_status()


# Functions are defined before they are called

def final_message():
    print("Python journey continues...")


final_message()