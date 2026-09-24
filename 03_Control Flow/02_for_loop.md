# For Loops

A `for` loop allows me to **repeat a block of code for each item in a sequence or other iterable**.

Before learning loops, if I wanted to print three values, I might write:

```python
print(1)
print(2)
print(3)
```

A `for` loop lets Python repeat the operation for me.

```python
for number in [1, 2, 3]:
    print(number)
```

Output:

```text
1
2
3
```

This is the basic idea behind a `for` loop:

**Take an item → run the code → take the next item → run the code again**

---

# Basic Syntax

The basic structure is:

```python
for variable in sequence:
    # code to repeat
```

For example:

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
mango
```

Here:

* `fruits` is the collection
* `fruit` is the loop variable
* `in` tells Python to take values from the collection
* the indented code runs once for each value

---

# How the Loop Works

For:

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

I can think about the process like this:

```text
Take "apple"
    ↓
print("apple")

Take "banana"
    ↓
print("banana")

Take "mango"
    ↓
print("mango")

No more items
    ↓
Loop ends
```

This way of thinking helped me understand that the loop variable changes as the loop moves through the collection.

---

# Looping Through a String

A string is also iterable, so I can loop through its characters.

```python
word = "Python"

for character in word:
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

This connects directly to the string indexing and character concepts I learned earlier.

---

# Looping Through a List

I can loop through each item in a list.

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
40
```

I don't need to manually access each index.

---

# Doing Something With Each Item

A loop becomes more useful when I perform an operation on every item.

```python
numbers = [1, 2, 3, 4]

for number in numbers:
    print(number * 2)
```

Output:

```text
2
4
6
8
```

Python takes one number at a time and performs the same operation.

---

# `range()`

`range()` is commonly used when I want a sequence of numbers.

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

An important detail is that `range(5)` starts at `0` and stops **before** `5`.

So:

```text
range(5)
→ 0, 1, 2, 3, 4
```

---

# `range(start, stop)`

I can specify where the sequence starts.

```python
for number in range(1, 6):
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

The stop value `6` is not included.

This follows the same idea I saw with slicing:

**start is included, stop is excluded.**

---

# `range(start, stop, step)`

I can also control how much the number changes each time.

```python
for number in range(1, 11, 2):
    print(number)
```

Output:

```text
1
3
5
7
9
```

Here:

* start = `1`
* stop = `11`
* step = `2`

---

# Counting Backwards

A negative step allows me to move backwards.

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

---

# Using `_` When I Don't Need the Loop Variable

Sometimes I only want to repeat something a certain number of times and don't care about the actual value.

In that situation, `_` is commonly used by convention.

```python
for _ in range(3):
    print("Hello Python")
```

Output:

```text
Hello Python
Hello Python
Hello Python
```

The `_` is simply communicating:

> "I need this repetition, but I don't need the value."

---

# Looping Through a Tuple

`for` loops work with tuples too.

```python
numbers = (10, 20, 30)

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
```

---

# Looping Through a Set

Sets can also be iterated over.

```python
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)
```

The order should not be assumed because sets do not provide a guaranteed positional order.

---

# Looping Through a Dictionary

Dictionaries behave slightly differently.

If I loop directly through a dictionary:

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

for key in student:
    print(key)
```

the loop goes through the **keys**.

To get values:

```python
for value in student.values():
    print(value)
```

To get both keys and values:

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Hanish
age 30
city Bengaluru
```

This connects directly to the `keys()`, `values()`, and `items()` methods I learned earlier.

---

# Using `if` Inside a `for` Loop

This is where loops and conditions start working together.

For example:

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(number)
```

Output:

```text
2
4
```

The loop checks every number, while the `if` decides whether that number should be printed.

The overall flow is:

```text
Take item
   ↓
Check condition
   ↓
True → Do something
False → Skip it
   ↓
Take next item
```

This is the beginning of more useful data processing.

---

# Accumulating a Result

A loop can also help me build a result step by step.

For example, calculating a total:

```python
numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total = total + number

print(total)
```

Output:

```text
100
```

The variable `total` changes during each iteration.

I can think of it as:

```text
Start total = 0

+ 10 → 10
+ 20 → 30
+ 30 → 60
+ 40 → 100
```

This pattern is very important for developing programming logic.

---

# Nested `for` Loops

A loop can exist inside another loop.

```python
for row in range(3):
    for column in range(3):
        print(row, column)
```

Output:

```text
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

The inner loop completes all of its iterations for each iteration of the outer loop.

Nested loops can be useful, but they can also become confusing. I will build more comfort with them through practice rather than trying to memorize the behavior.

---

# `for` Loop With `else`

Python also allows an `else` block after a `for` loop.

```python
for number in range(3):
    print(number)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
Loop completed
```

The `else` runs when the loop finishes normally.

This becomes more useful when combined with `break`, which I will learn separately.

---

# A Practical Example

Suppose I have marks:

```python
marks = [72, 85, 64, 91, 78]
```

I can check which marks are above `80`:

```python
for mark in marks:
    if mark > 80:
        print(mark)
```

Output:

```text
85
91
```

This is a simple example, but it is closer to the kind of repeated filtering I will eventually do with Data Science data.

---

# Another Practical Example

I can process strings inside a list:

```python
names = ["hanish", "rahul", "priya"]

for name in names:
    print(name.title())
```

Output:

```text
Hanish
Rahul
Priya
```

Here I am combining:

**List → Loop → String method → Output**

This is the kind of connection I want to become comfortable with.

---

# Common Beginner Mistakes

## Mistake 1 — Forgetting the colon

Incorrect:

```python
for number in numbers
    print(number)
```

Correct:

```python
for number in numbers:
    print(number)
```

---

## Mistake 2 — Incorrect indentation

Incorrect:

```python
for number in numbers:
print(number)
```

Correct:

```python
for number in numbers:
    print(number)
```

The indentation tells Python which statements belong to the loop.

---

## Mistake 3 — Confusing the loop variable with the collection

Consider:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(numbers)
```

This prints the **entire list** each time.

If I want each individual value:

```python
for number in numbers:
    print(number)
```

This distinction is simple but important.

---

## Mistake 4 — Misunderstanding `range()`

```python
range(5)
```

does **not** produce:

```text
1, 2, 3, 4, 5
```

It produces:

```text
0, 1, 2, 3, 4
```

Understanding this prevents many beginner mistakes.

---

# What I Noticed

Loops initially look simple:

```python
for item in collection:
    ...
```

But the important part is understanding what happens **one iteration at a time**.

I am trying not to think of a loop as something magical.

Instead:

> Python takes one item, executes the block, moves to the next item, and repeats.

That mental model makes loops easier to understand.

---

# What Connected With Previous Topics?

### Lists, Tuples, Sets & Strings

I can iterate through all of them.

### Dictionaries

I can work with keys, values, or key-value pairs.

### Operators

Operators can be used while processing each item.

### `if`

Conditions can decide what happens to each item.

### Variables

Variables can store information that changes during a loop, such as a running total.

This is where Python starts feeling more like a language for **processing data** rather than simply executing isolated statements.

---

# Practice

## Practice 1 — Print Numbers

Use a `for` loop to print numbers from `1` to `10`.

---

## Practice 2 — Print List Items

Create a list of five fruits and print each fruit using a `for` loop.

---

## Practice 3 — Squares

Create a list of numbers and print the square of each number.

---

## Practice 4 — Even Numbers

Using a loop, print only the even numbers from `1` to `20`.

---

## Practice 5 — Total

Create a list of numbers and calculate their total using a loop.

Don't use Python's built-in `sum()` yet. The goal is to understand the loop.

---

## Practice 6 — Filtering

Create a list of marks and print only the marks greater than `75`.

---

## Practice 7 — Strings

Create a list of names and print each name in title case.

---

## Practice 8 — Think Through the Loop

Without running the code first, predict the output:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number + 5)
```

Then run it and compare your prediction with the actual output.

---

## My Learning Note

> `for` loops introduced me to repetition in Python. The syntax looks simple, but I am learning that understanding what happens during each iteration is more important than memorizing the syntax. I want to become comfortable tracing a loop step by step.

---
