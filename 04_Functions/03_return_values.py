# ============================================
# Return Values
# ============================================


# print() vs return

def add_with_print(a, b):
    print(a + b)


result = add_with_print(10, 5)

print(result)


def add_with_return(a, b):
    return a + b


result = add_with_return(10, 5)

print(result)


# Returning a value

def add(a, b):
    return a + b


result = add(10, 5)

print(result)


# Returned value can be reused

def square(number):
    return number * number


result = square(5)

print(result)
print(result + 10)


# Return value can be used directly

result = add(10, 5) * 2

print(result)


# Return from an if statement

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even(10))
print(check_even(7))


# return ends the function

def test():
    print("Start")
    return
    print("End")


test()


# Function without a return value

def greet():
    print("Hello")


result = greet()

print(result)


# Returning different data types

def get_name():
    return "Hanish"


def get_age():
    return 30


def get_price():
    return 99.50


def is_adult():
    return True


print(get_name())
print(get_age())
print(get_price())
print(is_adult())


# Returning a list

def get_fruits():
    return ["apple", "banana", "mango"]


fruits = get_fruits()

print(fruits)
print(fruits[0])


# Returning multiple values

def get_numbers():
    return 10, 20


result = get_numbers()

print(result)


# Unpacking multiple returned values

a, b = get_numbers()

print(a)
print(b)


# Practical example: total price

def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(500, 3)

print(total)

discount = 100

final_price = total - discount

print(final_price)


# Practical example: grade

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"


grade = get_grade(82)

print(grade)


# Input + function + return

def calculate_square(number):
    return number * number


number = int(input("Enter a number: "))

result = calculate_square(number)

print(f"Square: {result}")