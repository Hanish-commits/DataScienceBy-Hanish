# ============================================
# If, Elif & Else
# ============================================

# Basic if statement

age = 20

if age >= 18:
    print("You are an adult")


# if with a False condition

age = 15

if age >= 18:
    print("You are an adult")


# if and else

age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")


# if, elif and else

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")


# Multiple elif conditions

marks = 62

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")


# Comparison operators in conditions

age = 25

if age == 25:
    print("Age is 25")

if age > 18:
    print("Age is above 18")

if age != 30:
    print("Age is not 30")


# Logical operators

age = 25

if age >= 18 and age <= 30:
    print("Age is between 18 and 30")


day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


is_raining = False

if not is_raining:
    print("You can go outside")


# Nested if

age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")


# Conditions with strings

username = "Hanish"

if username == "Hanish":
    print("Welcome back!")


# Checking text with in

message = "I am learning Python"

if "Python" in message:
    print("Python was found")


# Conditions with lists

fruits = ["apple", "banana", "mango"]

if "banana" in fruits:
    print("Banana is available")


# Conditions with dictionaries

student = {
    "name": "Hanish",
    "age": 30
}

if "age" in student:
    print("Age information is available")


# Truthy and falsy values

name = "Hanish"

if name:
    print("A name was provided")


name = ""

if name:
    print("A name was provided")
else:
    print("No name was provided")


# Input example

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")


# Practical example

age = int(input("Enter your age for ticket pricing: "))

if age < 5:
    price = 0
elif age < 18:
    price = 100
else:
    price = 200

print(f"Ticket price: ₹{price}")


# Demonstrating condition order

marks = 95

if marks >= 90:
    print("Excellent")
elif marks >= 50:
    print("Pass")