# Python Practice Answers — Complete Reference

This document contains reference solutions for the practice questions from the Python chapters completed so far.

**Chapters covered:**
1. Python Fundamentals
2. Working With Data
3. Control Flow
4. Functions
5. Intermediate Python — Comprehensions

> These are reference solutions. Try each problem yourself first, then compare your approach with the solution.

---

# 01 — Python Fundamentals

## 03 — Variables

### Practice 1 — Create a List of Variables

```python
name = "Hanish"
age = 30
city = "Bengaluru"

print(name)
print(age)
print(city)
```

### Practice 2 — Two Numbers

```python
a = 20
b = 5

print(a + b)
print(a - b)
print(a * b)
```

### Practice 3 — Update a Score

```python
score = 50

score += 25
score -= 10
score *= 2

print(score)
```

---

## 04 — Data Types

### Practice 1 — Personal Information

```python
name = "Hanish"
age = 30
height = 5.9
is_learning = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))
```

### Practice 2 — Number vs String

```python
number = 25
text = "25"

print(type(number))
print(type(text))
```

### Practice 3 — Change the Type

```python
value = 100

print(type(value))

value = "Python"

print(type(value))
```

---

## 05 — Operators

### Practice 1 — Calculator

```python
a = 20
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
```

### Practice 2 — Compare Age

```python
age = 20

print(age > 18)
print(age == 18)
print(age < 18)
```

### Practice 3 — Update Score

```python
score = 50

score += 25
score -= 10
score *= 2

print(score)
```

---

## 06 — Input & Output

### Practice 1 — Personal Information

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"My name is {name}, I am {age} years old, and I live in {city}.")
```

### Practice 2 — Add Two Numbers

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

### Practice 3 — Simple Bill

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total: ₹{total}")
```

### Practice 4 — Age Next Year

```python
age = int(input("Enter your current age: "))

print(f"Next year you will be {age + 1} years old.")
```

---

## 07 — Type Conversion

### Practice 1 — String to Integer

```python
number = "100"

number = int(number)

print(number)
print(type(number))
```

### Practice 2 — String to Float

```python
price = "49.99"

price = float(price)

print(price * 2)
```

### Practice 3 — Add Two User Inputs

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

### Practice 4 — Integer to String

```python
number = 100

text = str(number)

print(text)
print(type(text))
```

---

# 02 — Working With Data

## 01 — Strings

### Practice 1 — Indexing

```python
word = "Python"

print(word[0])
print(word[-1])
print(word[2])
```

Output:

```text
P
n
t
```

### Practice 2 — Slicing

```python
word = "Python"

print(word[:3])
print(word[3:])
print(word[::-1])
```

Output:

```text
Pyt
hon
nohtyP
```

### Practice 3 — String Methods

```python
text = "   PyThOn   "

text = text.strip()

print(text.lower())
print(text.upper())
```

### Practice 4 — Searching

```python
sentence = "Data science is interesting and data science is useful"

print("science" in sentence)
print(sentence.count("data"))
```

### Practice 5 — Split

```python
sentence = "Python is my first programming language"

words = sentence.split()

print(words)
```

### Practice 6 — Name Formatting

```python
name = input("Enter your full name: ")

name = name.strip()
name = name.title()

print(f"Hello, {name}!")
```

---

## 02 — Lists

### Practice 1 — Create a Food List

```python
foods = ["pizza", "burger", "pasta", "biryani", "sandwich"]

print(foods)
print(foods[0])
print(foods[-1])
print(len(foods))
```

### Practice 2 — Modify a List

```python
numbers = [10, 20, 30, 40, 50]

numbers[2] = 35
numbers.append(60)
numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 35, 40, 50, 60]
```

### Practice 3 — `append()` vs `extend()`

```python
list_one = ["apple", "banana"]
list_one.append(["mango", "orange"])

print(list_one)

list_two = ["apple", "banana"]
list_two.extend(["mango", "orange"])

print(list_two)
```

Output:

```text
['apple', 'banana', ['mango', 'orange']]
['apple', 'banana', 'mango', 'orange']
```

### Practice 4 — Sort

```python
numbers = [40, 10, 30, 20]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
```

Output:

```text
[10, 20, 30, 40]
[40, 30, 20, 10]
```

### Practice 5 — Search & Count

```python
numbers = [10, 20, 10, 30, 10]

print(20 in numbers)
print(numbers.index(20))
print(numbers.count(10))
```

Output:

```text
True
1
3
```

### Practice 6 — Shopping Cart

```python
cart = ["milk", "bread", "eggs"]

cart.append("butter")
cart.remove("bread")

print("eggs" in cart)
print(cart)
```

---

## 03 — Tuples

### Practice 1 — Create a Tuple

```python
student = ("Hanish", 30, "Bengaluru")

print(student)
print(type(student))
```

### Practice 2 — Indexing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[-1])
print(numbers[2])
```

### Practice 3 — Slicing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
print(numbers[-3:])
print(numbers[::-1])
```

Output:

```text
(10, 20, 30)
(30, 40, 50)
(50, 40, 30, 20, 10)
```

### Practice 4 — Unpacking

```python
student = ("Hanish", 30, "Data Science")

name, age, course = student

print(name)
print(age)
print(course)
```

### Practice 5 — List to Tuple

```python
items = ["Python", "SQL", "Pandas"]

print(type(items))

items = tuple(items)

print(items)
print(type(items))
```

### Practice 6 — Choose the Data Structure

**A — Shopping cart:** List

```python
cart = ["milk", "bread", "eggs"]
```

**B — Fixed coordinates:** Tuple

```python
coordinates = (12.9716, 77.5946)
```

Reason:

- A shopping cart may change.
- Coordinates can represent a fixed collection of values.

---

## 04 — Sets

### Practice 1 — Remove Duplicates

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)
```

### Practice 2 — Add, Remove & Check

```python
fruits = {"apple", "banana", "mango"}

fruits.add("orange")
fruits.remove("banana")

print("mango" in fruits)
print(fruits)
```

### Practice 3 — Union & Intersection

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b)
print(set_a & set_b)
```

Conceptually:

```text
Union        → {1, 2, 3, 4, 5, 6}
Intersection → {3, 4}
```

### Practice 4 — Difference

```python
class_a = {"Hanish", "Rahul", "Aman", "Priya"}
class_b = {"Priya", "Aman", "Riya", "Karan"}

only_a = class_a - class_b

print(only_a)
```

Conceptually:

```text
{"Hanish", "Rahul"}
```

### Practice 5 — Choose the Data Structure

**A — Unique email addresses:** Set

```python
emails = {"a@example.com", "b@example.com"}
```

**B — Student information with labels:** Dictionary

```python
student = {
    "name": "Hanish",
    "age": 30
}
```

**C — Shopping list where order matters:** List

```python
shopping_list = ["milk", "bread", "eggs"]
```

**D — Fixed coordinates:** Tuple

```python
coordinates = (12.9716, 77.5946)
```

---

## 05 — Dictionaries

### Practice 1 — Student Dictionary

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru",
    "course": "Data Science"
}

print(student["name"])
print(student["age"])
print(student["city"])
print(student["course"])
```

### Practice 2 — Modify a Dictionary

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

student["age"] = 31
student["course"] = "Data Science"

del student["city"]

print(student)
```

### Practice 3 — Dictionary Methods

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
```

### Practice 4 — Nested List

```python
student = {
    "name": "Hanish",
    "skills": ["Python", "SQL", "Pandas"]
}

print(student["skills"])
print(student["skills"][0])
```

### Practice 5 — Product Calculation

```python
product = {
    "name": "Laptop",
    "price": 75000,
    "quantity": 2
}

total = product["price"] * product["quantity"]

print(total)
```

### Practice 6 — Choose the Data Structure

**A — Unique email addresses:** Set

**B — Student information with labels:** Dictionary

**C — Ordered shopping list:** List

**D — Fixed coordinates:** Tuple

---

# 03 — Control Flow

## 01 — If, Elif & Else

### Practice 1 — Positive, Negative or Zero

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Practice 2 — Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Practice 3 — Age Category

One valid approach:

```python
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

### Practice 4 — Grade Calculator

```python
marks = float(input("Enter marks: "))

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
```

### Practice 5 — Login Check

```python
stored_username = "admin"
stored_password = "python123"

username = input("Username: ")
password = input("Password: ")

if username == stored_username and password == stored_password:
    print("Login successful")
else:
    print("Invalid username or password")
```

### Practice 6 — Temperature

One valid set of ranges:

```python
temperature = float(input("Enter temperature: "))

if temperature < 10:
    print("Cold")
elif temperature < 25:
    print("Cool")
elif temperature < 35:
    print("Warm")
else:
    print("Hot")
```

---

## 02 — For Loops

### Practice 1 — Print 1 to 10

```python
for number in range(1, 11):
    print(number)
```

### Practice 2 — Print Fruits

```python
fruits = ["apple", "banana", "mango", "orange", "grape"]

for fruit in fruits:
    print(fruit)
```

### Practice 3 — Squares

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number ** 2)
```

### Practice 4 — Even Numbers

```python
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
```

### Practice 5 — Total

```python
numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print(total)
```

### Practice 6 — Filter Marks

```python
marks = [72, 85, 64, 91, 78]

for mark in marks:
    if mark > 75:
        print(mark)
```

### Practice 7 — Title Case Names

```python
names = ["hanish", "rahul", "priya", "aman"]

for name in names:
    print(name.title())
```

### Practice 8 — Predict the Output

Code:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number + 5)
```

Output:

```text
15
25
35
```

---

## 03 — While Loops

### Practice 1 — Count to 10

```python
number = 1

while number <= 10:
    print(number)
    number += 1
```

### Practice 2 — Countdown

```python
number = 5

while number >= 1:
    print(number)
    number -= 1
```

### Practice 3 — Even Numbers

```python
number = 1

while number <= 20:
    if number % 2 == 0:
        print(number)

    number += 1
```

### Practice 4 — Sum 1 to 10

```python
number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print(total)
```

Output:

```text
55
```

### Practice 5 — Positive Input

```python
number = int(input("Enter a positive number: "))

while number <= 0:
    number = int(input("Please enter a positive number: "))

print(f"You entered {number}")
```

### Practice 6 — Password

```python
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")
```

### Practice 7 — Predict the Output

Code:

```python
number = 1

while number <= 4:
    print(number)
    number += 1
```

Output:

```text
1
2
3
4
```

### Practice 8 — Find the Problem

Problematic code:

```python
number = 10

while number <= 20:
    print(number)
    number -= 1
```

Problem:

`number` is decreasing, so it moves away from `20`.

Correct version:

```python
number = 10

while number <= 20:
    print(number)
    number += 1
```

---

## 04 — Break, Continue & Pass

### Practice 1 — Break

```python
for number in range(1, 11):
    if number == 6:
        break

    print(number)
```

Output:

```text
1
2
3
4
5
```

### Practice 2 — Continue

```python
for number in range(1, 11):
    if number == 5:
        continue

    print(number)
```

Output:

```text
1
2
3
4
6
7
8
9
10
```

### Practice 3 — Search for Rahul

```python
names = ["Hanish", "Rahul", "Priya", "Aman"]

for name in names:
    if name == "Rahul":
        print("Found")
        break
```

### Practice 4 — Print Positive Numbers

```python
numbers = [10, -5, 20, -10, 30]

for number in numbers:
    if number < 0:
        continue

    print(number)
```

Output:

```text
10
20
30
```

### Practice 5 — Understand `pass`

```python
numbers = [1, 2, 3]

for number in numbers:
    if number == 2:
        pass

    print(number)
```

Output:

```text
1
2
3
```

`pass` does nothing.

Compare with:

```python
for number in numbers:
    if number == 2:
        continue

    print(number)
```

Output:

```text
1
3
```

### Practice 6 — Exit With User Input

```python
while True:
    command = input("Enter something (or 'exit' to stop): ")

    if command == "exit":
        break

    print(f"You entered: {command}")

print("Program ended")
```

### Practice 7 — Predict the Output

Code:

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

### Practice 8 — Explain the Difference

```text
break
→ stops the entire loop

continue
→ skips the current iteration

pass
→ does nothing
```

---

# 04 — Functions

## 01 — Function Basics

### Practice 1 — Simple Function

```python
def greet():
    print("Hello Python")

greet()
greet()
greet()
```

### Practice 2 — Personal Information

```python
def show_profile():
    print("Name: Hanish")
    print("Goal: Become a Data Scientist")
    print("Learning: Python")

show_profile()
```

### Practice 3 — Function With a Loop

```python
def print_numbers():
    for number in range(1, 6):
        print(number)

print_numbers()
```

### Practice 4 — Function With a Condition

```python
def check_age():
    age = 20

    if age >= 18:
        print("Adult")
    else:
        print("Not an adult")

check_age()
```

### Practice 5 — Two Functions

```python
def show_python():
    print("I am learning Python")

def show_data_science():
    print("I am working toward Data Science")

show_python()
show_data_science()
```

### Practice 6 — Predict the Output

Code:

```python
def test():
    print("A")
    print("B")

print("Start")
test()
print("End")
```

Output:

```text
Start
A
B
End
```

---

## 02 — Parameters & Arguments

### Practice 1 — One Parameter

```python
def greet(name):
    print(f"Hello {name}")

greet("Hanish")
greet("Rahul")
greet("Priya")
```

### Practice 2 — Two Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Practice 3 — Default Parameter

```python
def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Hanish")
```

### Practice 4 — Keyword Arguments

```python
def profile(name, age, city):
    print(name)
    print(age)
    print(city)

profile(
    age=30,
    city="Bengaluru",
    name="Hanish"
)
```

### Practice 5 — Even or Odd

```python
def check_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even(10)
check_even(7)
```

### Practice 6 — Calculate Total

```python
def calculate_total(price, quantity):
    print(price * quantity)

calculate_total(500, 3)
```

### Practice 7 — Input + Function

```python
def greet(name):
    print(f"Hello {name}")

name = input("Enter your name: ")

greet(name)
```

### Practice 8 — Predict the Output

Code:

```python
def introduce(name, course="Python"):
    print(f"{name} is learning {course}")

introduce("Hanish")
introduce("Rahul", "SQL")
```

Output:

```text
Hanish is learning Python
Rahul is learning SQL
```

---

## 03 — Return Values

### Practice 1 — Return a Sum

```python
def add(a, b):
    return a + b

result = add(10, 5)

print(result)
```

### Practice 2 — Square

```python
def square(number):
    return number * number

result = square(5)

print(result)
print(result + 10)
```

Output:

```text
25
35
```

### Practice 3 — Even or Odd

```python
def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(10))
print(check_even(7))
```

### Practice 4 — Total + Discount

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)
final_price = total - 100

print(final_price)
```

### Practice 5 — Multiple Returned Values

```python
def get_details():
    return "Hanish", 30, "Python"

name, age, language = get_details()

print(name)
print(age)
print(language)
```

### Practice 6 — Print vs Return

```python
def show_result():
    print(10 + 5)

def get_result():
    return 10 + 5

show_result()

result = get_result()

print(result)
```

### Practice 7 — Predict the Output

Code:

```python
def test():
    print("Start")
    return "B"
    print("C")

result = test()

print(result)
```

Output:

```text
Start
B
```

`print("C")` never runs because `return` ends the function.

### Practice 8 — Follow the Value

```python
def double(number):
    return number * 2

result = double(10)
final = result + 5

print(final)
```

Output:

```text
25
```

Flow:

```text
10
↓
20
↓
25
```

---

## 04 — Scope

### Practice 1 — Local Variable

```python
def test():
    name = "Hanish"
    print(name)

test()

# print(name)  # NameError
```

The variable `name` is local to the function.

### Practice 2 — Global Variable

```python
name = "Hanish"

def show_name():
    print(name)

show_name()
```

### Practice 3 — Same Name

```python
name = "Global"

def test():
    name = "Local"
    print(name)

test()
print(name)
```

Output:

```text
Local
Global
```

### Practice 4 — `global`

```python
count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)
```

Output:

```text
20
```

### Practice 5 — Global vs Parameter

Using a parameter:

```python
def calculate(price, quantity):
    return price * quantity

print(calculate(500, 3))
```

This is usually easier to reuse because the function clearly states what data it needs.

### Practice 6 — Return + Scope

```python
def get_name():
    name = "Hanish"
    return name

result = get_name()

print(result)
```

`name` remains local; its value is returned and stored in `result`.

### Practice 7 — LEGB

```python
value = "global"

def outer():
    value = "enclosing"

    def inner():
        value = "local"
        print(value)

    inner()

outer()
```

Output:

```text
local
```

---

## 05 — Advanced Function Arguments

### Practice 1 — `*args`

```python
def show_numbers(*args):
    print(args)

show_numbers(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

### Practice 2 — Count Arguments

```python
def count_arguments(*args):
    print(len(args))

count_arguments(10, 20, 30, 40)
```

Output:

```text
4
```

### Practice 3 — Total With `*args`

```python
def calculate_total(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(calculate_total(10, 20))
print(calculate_total(10, 20, 30))
```

### Practice 4 — `**kwargs`

```python
def show_profile(**kwargs):
    print(kwargs)

show_profile(
    name="Hanish",
    age=30,
    city="Bengaluru",
    course="Data Science"
)
```

### Practice 5 — Loop Through `kwargs`

```python
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_profile(
    name="Hanish",
    age=30,
    city="Bengaluru"
)
```

### Practice 6 — Combine `*args` and `**kwargs`

```python
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
```

### Practice 7 — List Unpacking

```python
numbers = [10, 20, 30]

def add(a, b, c):
    return a + b + c

print(add(*numbers))
```

Output:

```text
60
```

### Practice 8 — Dictionary Unpacking

```python
details = {
    "name": "Hanish",
    "age": 30
}

def show_profile(name, age):
    print(name, age)

show_profile(**details)
```

### Practice 9 — Predict the Output

Code:

```python
def test(*args):
    print(args)
    print(type(args))

test(10, 20, 30)
```

Output:

```text
(10, 20, 30)
<class 'tuple'>
```

### Practice 10 — Explain the Symbols

```text
*args
→ collects positional arguments into a tuple

**kwargs
→ collects keyword arguments into a dictionary

*list_name
→ unpacks a list/tuple into positional arguments

**dict_name
→ unpacks a dictionary into keyword arguments
```

---

# 05 — Intermediate Python

## 01 — Comprehensions

### Practice 1 — Squares

Normal loop:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

List comprehension:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

### Practice 2 — Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

### Practice 3 — Word Lengths

```python
words = ["Python", "SQL", "Pandas", "AI"]

lengths = [len(word) for word in words]

print(lengths)
```

Output:

```text
[6, 3, 6, 2]
```

### Practice 4 — Filter Names

```python
names = ["Hanish", "Aman", "Rahul", "Priya", "Riya"]

result = [name for name in names if len(name) > 4]

print(result)
```

### Practice 5 — Even / Odd Labels

```python
numbers = [1, 2, 3, 4, 5]

labels = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(labels)
```

Output:

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

### Practice 6 — Set Comprehension

```python
numbers = [1, 2, 2, 3, 3, 4]

squares = {number ** 2 for number in numbers}

print(squares)
```

### Practice 7 — Dictionary Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)
```

Result:

```text
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

### Practice 8 — Predict the Output

Code:

```python
numbers = [1, 2, 3, 4, 5]

result = [number * 10 for number in numbers if number > 2]

print(result)
```

Output:

```text
[30, 40, 50]
```

### Practice 9 — Rewrite as a Comprehension

Original:

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number * 10)
```

Comprehension:

```python
numbers = [1, 2, 3, 4, 5]

result = [number * 10 for number in numbers if number % 2 == 0]

print(result)
```

### Practice 10 — Choose Readability

There is no single code answer here.

The rule is:

```text
Use a comprehension when it makes a simple transformation
or filtering operation easier to read.

Use a normal loop when the logic becomes complicated,
multi-step, or difficult to understand in one line.
```

For example, this is readable:

```python
squares = [number ** 2 for number in numbers]
```

But a complicated multi-condition comprehension may be clearer as a normal loop.

---

# Quick Reference — Most Important Patterns

## Variable

```python
name = "Hanish"
```

## Condition

```python
if condition:
    ...
```

## For loop

```python
for item in collection:
    ...
```

## While loop

```python
while condition:
    ...
```

## Function

```python
def function_name():
    ...
```

## Parameter

```python
def greet(name):
    ...
```

## Return

```python
def add(a, b):
    return a + b
```

## `*args`

```python
def function(*args):
    ...
```

## `**kwargs`

```python
def function(**kwargs):
    ...
```

## List comprehension

```python
result = [expression for item in iterable]
```

## List comprehension with filtering

```python
result = [expression for item in iterable if condition]
```

## Dictionary comprehension

```python
result = {
    key: value
    for item in iterable
}
```

---

# Reminder

These solutions are not meant to replace the practice.

A better learning cycle is:

```text
Try yourself
    ↓
Run the code
    ↓
Get an error / unexpected output
    ↓
Debug
    ↓
Compare with the reference
    ↓
Understand why
```

The goal is not just to get the answer.

The goal is to eventually be able to write the answer without looking at it.
