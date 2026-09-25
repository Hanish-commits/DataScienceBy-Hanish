# ============================================
# Comprehensions
# ============================================


# --------------------------------------------
# List comprehension
# --------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# Normal loop equivalent

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)


# Doubling values

doubled = [number * 2 for number in numbers]

print(doubled)


# Length of each word

words = ["Python", "SQL", "Pandas", "AI"]

lengths = [len(word) for word in words]

print(lengths)


# --------------------------------------------
# List comprehension with a condition
# --------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# Filter strings

names = ["Hanish", "Rahul", "Aman", "Priya"]

long_names = [
    name
    for name in names
    if len(name) > 4
]

print(long_names)


# Transform and filter

numbers = [1, 2, 3, 4, 5, 6]

squares_of_even = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(squares_of_even)


# --------------------------------------------
# if / else inside a comprehension
# --------------------------------------------

numbers = [1, 2, 3, 4, 5]

labels = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(labels)


# --------------------------------------------
# Nested list comprehension
# --------------------------------------------

matrix = [
    [1, 2],
    [3, 4]
]

flattened = [
    number
    for row in matrix
    for number in row
]

print(flattened)


# --------------------------------------------
# Set comprehension
# --------------------------------------------

numbers = [1, 2, 2, 3, 3, 4]

unique_squares = {
    number ** 2
    for number in numbers
}

print(unique_squares)


# --------------------------------------------
# Dictionary comprehension
# --------------------------------------------

numbers = [1, 2, 3, 4]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# Dictionary comprehension with a condition

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)


# --------------------------------------------
# Dictionary comprehension with zip()
# --------------------------------------------

names = ["Hanish", "Rahul", "Priya"]
scores = [85, 78, 92]

student_scores = {
    name: score
    for name, score in zip(names, scores)
}

print(student_scores)


# --------------------------------------------
# A simple practical example
# --------------------------------------------

prices = [100, 250, 500, 750]

discounted_prices = [
    price * 0.9
    for price in prices
    if price >= 250
]

print(discounted_prices)