# Type Conversion in Python

# String to integer

number = "10"

number = int(number)

print(number)
print(type(number))


# String to float

price = "99.50"

price = float(price)

print(price)
print(type(price))


# Integer to string

age = 30

age_text = str(age)

print(age_text)
print(type(age_text))


# Converting values to Boolean

print(bool(1))
print(bool(0))


# Type conversion with input

age = int(input("Enter your age: "))

print(age + 1)


# Comparing input with and without conversion

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)


num1 = int(input("Enter first number again: "))
num2 = int(input("Enter second number again: "))

print(num1 + num2)


# Multiple-step conversion

number = int(float("10.5"))

print(number)