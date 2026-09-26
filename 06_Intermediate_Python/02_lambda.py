# ============================================
# Lambda Functions
# ============================================


# Basic lambda

square = lambda number: number ** 2

print(square(5))


# One parameter

double = lambda number: number * 2

print(double(10))


cube = lambda number: number ** 3

print(cube(3))


# Multiple parameters

add = lambda a, b: a + b

print(add(10, 20))


multiply = lambda a, b: a * b

print(multiply(5, 4))


# Lambda with no parameters

greeting = lambda: "Hello Python"

print(greeting())


# Lambda with a condition

check_even = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check_even(10))
print(check_even(7))


# Lambda with strings

get_length = lambda text: len(text)

print(get_length("Python"))


to_upper = lambda text: text.upper()

print(to_upper("python"))


# Lambda with a list

get_first = lambda items: items[0]

numbers = [10, 20, 30]

print(get_first(numbers))


# ============================================
# Lambda with sorted()
# ============================================

students = [
    ("Hanish", 85),
    ("Rahul", 72),
    ("Priya", 92)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1]
)

print(students_sorted)


# Sort in descending order

students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(students_sorted)


# ============================================
# Sorting dictionary items
# ============================================

students = {
    "Hanish": 85,
    "Rahul": 72,
    "Priya": 92
}

students_sorted = sorted(
    students.items(),
    key=lambda item: item[1]
)

print(students_sorted)


# ============================================
# Lambda with map()
# ============================================

numbers = [1, 2, 3, 4]

result = map(lambda number: number * 2, numbers)

print(list(result))


# ============================================
# Lambda with filter()
# ============================================

numbers = [1, 2, 3, 4, 5, 6]

result = filter(
    lambda number: number % 2 == 0,
    numbers
)

print(list(result))


# ============================================
# Functions as values
# ============================================

def normal_square(number):
    return number ** 2


operation = normal_square

print(operation(5))


# Lambda stored in a variable

operation = lambda number: number ** 2

print(operation(5))


# ============================================
# Passing a function to another function
# ============================================

def apply_operation(number, operation):
    return operation(number)


def square_number(number):
    return number ** 2


print(apply_operation(5, square_number))

print(
    apply_operation(
        5,
        lambda number: number ** 2
    )
)


# ============================================
# Practical example: sort products
# ============================================

products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Mouse", "price": 1500},
    {"name": "Keyboard", "price": 3000}
]

sorted_products = sorted(
    products,
    key=lambda product: product["price"]
)

print(sorted_products)