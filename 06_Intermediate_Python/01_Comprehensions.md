# Comprehensions

I have already learned how to use loops to process collections.

For example, if I want to create a list containing the squares of numbers, I can write:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Python provides a more compact way of writing this using a **list comprehension**.

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

The result is the same.

The important thing is that I should learn comprehensions as a **different way of expressing logic I already understand**, not as something to memorize without understanding the underlying loop.

---

# What Is a Comprehension?

A comprehension is a compact way to create a new collection from an existing iterable.

The main types I am learning here are:

* List comprehensions
* Set comprehensions
* Dictionary comprehensions

There is also a related concept called a **generator expression**, which I will explore later with iterators and generators.

---

# List Comprehensions

The basic structure is:

```python
[expression for item in iterable]
```

For example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

I can read it roughly as:

> For each `number` in `numbers`, put `number ** 2` into the new list.

---

# Understanding the Parts

Consider:

```python
squares = [number ** 2 for number in numbers]
```

There are three important pieces:

```text
number ** 2
     ↑
 expression

for number
     ↑
 loop variable

in numbers
     ↑
 source iterable
```

So the comprehension is essentially a compact form of:

```python
squares = []

for number in numbers:
    squares.append(number ** 2)
```

Understanding this connection is more important than simply memorizing the syntax.

---

# A Simple Example

I can create a list of doubled values:

```python
numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)
```

Output:

```text
[2, 4, 6, 8, 10]
```

---

# Working With Strings

Comprehensions aren't limited to numbers.

I can create a list containing the length of each word:

```python
words = ["Python", "SQL", "Pandas", "AI"]

lengths = [len(word) for word in words]

print(lengths)
```

Output:

```text
[6, 3, 6, 2]
```

This shows that the expression can contain functions or operations I already know.

---

# List Comprehension With a Condition

I can add an `if` condition.

The basic structure becomes:

```python
[expression for item in iterable if condition]
```

For example, I can select only even numbers:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

This is similar to:

```python
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
```

Again, the comprehension is not introducing new logic. It is expressing familiar logic more compactly.

---

# Filtering Strings

The same idea works with strings.

```python
names = ["Hanish", "Rahul", "Aman", "Priya"]

long_names = [name for name in names if len(name) > 4]

print(long_names)
```

Output:

```text
['Hanish', 'Rahul', 'Priya']
```

The condition determines which values make it into the new list.

---

# Transforming and Filtering at the Same Time

I can also transform a value while filtering it.

```python
numbers = [1, 2, 3, 4, 5, 6]

squares_of_even = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(squares_of_even)
```

Output:

```text
[4, 16, 36]
```

The flow is:

```text
Take number
   ↓
Is it even?
   ↓
Yes
   ↓
Square it
   ↓
Add result to new list
```

---

# `if` / `else` Inside a List Comprehension

There is another form where I use `if` and `else` to decide **what value should be produced**.

For example:

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

This is different from the earlier filtering example.

### Filtering

```python
[number for number in numbers if condition]
```

This decides **whether an item is included**.

### Conditional expression

```python
[value_if_true if condition else value_if_false for item in iterable]
```

This decides **what value is produced**.

That distinction is important.

---

# Nested List Comprehensions

I can create nested structures with comprehensions.

For example:

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

I can flatten it:

```python
matrix = [
    [1, 2],
    [3, 4]
]

flattened = [number for row in matrix for number in row]

print(flattened)
```

Output:

```text
[1, 2, 3, 4]
```

This is compact, but it can become difficult to read.

At my current stage, I should not use nested comprehensions just because I can. Readability still matters.

---

# Set Comprehensions

A similar syntax can create sets.

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_squares = {number ** 2 for number in numbers}

print(unique_squares)
```

The result is a set, so duplicate results are removed.

Conceptually:

```text
List comprehension → []
Set comprehension  → {}
```

But `{}` by itself still creates an empty dictionary, so the context matters.

---

# Dictionary Comprehensions

Dictionary comprehensions allow me to create dictionaries in a compact way.

The general structure is:

```python
{key_expression: value_expression for item in iterable}
```

For example:

```python
numbers = [1, 2, 3, 4]

squares = {number: number ** 2 for number in numbers}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

Here:

```text
number      → key
number ** 2 → value
```

---

# Dictionary Comprehension With a Condition

I can also filter values.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)
```

Output:

```text
{2: 4, 4: 16, 6: 36}
```

---

# Creating a Dictionary From Two Lists

Suppose I have:

```python
names = ["Hanish", "Rahul", "Priya"]
scores = [85, 78, 92]
```

I can combine them using `zip()`:

```python
names = ["Hanish", "Rahul", "Priya"]
scores = [85, 78, 92]

student_scores = {
    name: score
    for name, score in zip(names, scores)
}

print(student_scores)
```

Output:

```text
{'Hanish': 85, 'Rahul': 78, 'Priya': 92}
```

I will explore `zip()` in more detail in a later topic.

---

# Why Not Always Use Comprehensions?

A comprehension can make code shorter, but shorter does not automatically mean better.

This:

```python
squares = [number ** 2 for number in numbers]
```

is easy to read.

But something extremely complicated such as:

```python
result = [x ** 2 if x % 2 == 0 else x * 3 for x in numbers if x > 10 and x != 15]
```

can become harder to understand.

In such a situation, a normal loop may actually be clearer.

My rule should be:

> Use comprehensions when they make simple transformation or filtering easier to read.

---

# Comprehension vs Normal Loop

Suppose:

```python
numbers = [1, 2, 3, 4, 5]
```

### Normal loop

```python
squares = []

for number in numbers:
    squares.append(number ** 2)
```

### List comprehension

```python
squares = [number ** 2 for number in numbers]
```

Both are valid.

The comprehension is simply more compact.

As I gain experience, I want to understand both forms rather than using comprehensions blindly.

---

# What I Noticed

Comprehensions initially look like a completely new syntax.

But after breaking them down, I can see that they combine concepts I already know:

**List + loop + expression**

and sometimes:

**List + loop + condition**

So the challenge is less about learning a new programming idea and more about learning a new way of expressing an idea.

---

# What Connected With Previous Topics?

### Lists

List comprehensions create lists.

### Sets

Set comprehensions create sets.

### Dictionaries

Dictionary comprehensions create dictionaries.

### Loops

The `for` part represents iteration.

### Conditions

An `if` can filter or control the result.

### Operators

Expressions can use the operators I already know.

### `zip()`

Dictionary comprehensions can work with zipped data.

This is a good example of intermediate Python being built from the foundations I already learned.

---

# Practice

## Practice 1 — Squares

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

create a list of squares using:

1. a normal `for` loop
2. a list comprehension

Compare the two.

---

## Practice 2 — Even Numbers

Create a list containing only the even numbers from:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Use a list comprehension.

---

## Practice 3 — Word Lengths

Given:

```python
words = ["Python", "SQL", "Pandas", "AI"]
```

create a list containing the length of each word.

---

## Practice 4 — Filter Names

Given:

```python
names = ["Hanish", "Aman", "Rahul", "Priya", "Riya"]
```

create a new list containing names longer than four characters.

---

## Practice 5 — Even / Odd Labels

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

create:

```text
["Odd", "Even", "Odd", "Even", "Odd"]
```

using a list comprehension.

---

## Practice 6 — Set Comprehension

Given:

```python
numbers = [1, 2, 2, 3, 3, 4]
```

create a set containing their squares.

---

## Practice 7 — Dictionary Comprehension

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

create:

```text
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

---

## Practice 8 — Think Before Running

What will this produce?

```python
numbers = [1, 2, 3, 4, 5]

result = [number * 10 for number in numbers if number > 2]

print(result)
```

Predict the output before running it.

---

## Practice 9 — Rewrite It

Convert this loop into a list comprehension:

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number * 10)
```

---

## Practice 10 — Choose Readability

Look at a comprehension you wrote and ask:

> Is this actually easier to understand than the equivalent loop?

This is an important habit. The goal is not to make every piece of Python code as short as possible.

---

## My Learning Note

> Comprehensions looked like new syntax at first, but I realized they are mainly a compact way of expressing loops and conditions I already understand. I want to use them when they make the code clearer, not just because they make the code shorter.

---
