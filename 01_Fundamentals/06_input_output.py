# Python Input and Output

# Basic output

print("Hello Python")


# Printing variables

name = "Hanish"
age = 30

print(name)
print(age)
print(name, age)


# Taking string input

user_name = input("Enter your name: ")

print(user_name)


# Checking the type returned by input()

user_age = input("Enter your age: ")

print(user_age)
print(type(user_age))


# Taking integer input

age = int(input("Enter your age: "))

print(age + 1)


# Taking float input

price = float(input("Enter the price: "))

print(price)
print(type(price))


# Input -> Process -> Output

item_price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = item_price * quantity

print(total)


# Using an f-string

name = "Hanish"
age = 30

print(f"My name is {name} and I am {age} years old.")