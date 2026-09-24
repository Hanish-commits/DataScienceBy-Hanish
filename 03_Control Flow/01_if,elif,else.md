# If, Elif & Else

Until now, most of my Python programs have followed instructions from top to bottom.

Now I am learning how to make a program **choose what to do based on a condition**.

This is the beginning of **control flow**.

For example:

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Python checks the condition and executes the indented code only when the condition is `True`.

---

# What is a Condition?

A condition is an expression that evaluates to either:

```text
True
False
```

For example:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

This connects directly to the comparison operators I learned earlier.

```python
age >= 18
age == 20
age < 25
```

These expressions produce Boolean results that Python can use to make decisions.

---

# The `if` Statement

The basic structure is:

```python
if condition:
    # code to execute
```

Example:

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Output:

```text
You are an adult
```

If the condition is `False`, Python simply skips the indented block.

```python
age = 15

if age >= 18:
    print("You are an adult")
```

There is no output because the condition is `False`.

---

# Indentation Matters

Python uses **indentation** to define which statements belong to the `if` block.

```python
age = 20

if age >= 18:
    print("You are an adult")
```

The `print()` statement is indented, so Python knows it belongs to the `if` statement.

This would be invalid:

```python
age = 20

if age >= 18:
print("You are an adult")
```

Python raises an `IndentationError`.

This was an important change from the earlier topics because indentation is now part of the program's structure.

---

# The `else` Statement

Sometimes I want one thing to happen when the condition is `True` and something else when it is `False`.

That's where `else` is useful.

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
```

Output:

```text
You are not an adult
```

The `else` block runs when the `if` condition is `False`.

---

# The `elif` Statement

Sometimes there are more than two possible situations.

I can use `elif`, which means **"else if"**.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

Output:

```text
Grade B
```

Python checks the conditions from top to bottom.

As soon as it finds a `True` condition, it executes that block and skips the remaining branches.

---

# Multiple `elif` Conditions

I can have more than one `elif`.

```python
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
```

Output:

```text
Grade C
```

The order of the conditions matters.

---

# How Python Chooses a Branch

Suppose:

```python
marks = 85
```

Python checks:

```text
marks >= 90  → False
marks >= 75  → True
```

It executes the `elif marks >= 75` block and stops checking the remaining branches.

So the flow is:

```text
Start
  ↓
Check condition
  ↓
True? ── Yes → Execute block → End
  │
  No
  ↓
Check next condition
  ↓
True? ── Yes → Execute block → End
  │
  No
  ↓
else → Execute fallback block
```

This is the basic decision-making pattern I am learning.

---

# Comparison Operators in Conditions

The comparison operators I learned earlier can be used directly in conditions.

```python
age = 25

if age == 25:
    print("Age is 25")

if age > 18:
    print("Age is above 18")

if age != 30:
    print("Age is not 30")
```

The condition determines whether each block runs.

---

# Logical Operators in Conditions

I can also combine conditions using:

* `and`
* `or`
* `not`

### Using `and`

Both conditions must be `True`.

```python
age = 25

if age >= 18 and age <= 30:
    print("Age is between 18 and 30")
```

### Using `or`

At least one condition must be `True`.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### Using `not`

`not` reverses a Boolean result.

```python
is_raining = False

if not is_raining:
    print("You can go outside")
```

These operators allow me to build more useful conditions.

---

# Nested `if`

An `if` statement can exist inside another `if` statement.

This is called a **nested `if`**.

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

Here, the second condition is checked only if the first condition is `True`.

Nested conditions can be useful, but too much nesting can make code harder to read.

For now, I mainly want to understand how the structure works.

---

# Conditions With Strings

Conditions aren't limited to numbers.

I can compare strings too.

```python
username = "Hanish"

if username == "Hanish":
    print("Welcome back!")
```

Output:

```text
Welcome back!
```

I can also check whether text exists inside another string.

```python
message = "I am learning Python"

if "Python" in message:
    print("Python was found")
```

This connects directly to the string concepts I learned earlier.

---

# Conditions With Lists

The membership operator also works with lists.

```python
fruits = ["apple", "banana", "mango"]

if "banana" in fruits:
    print("Banana is available")
```

Output:

```text
Banana is available
```

This shows how earlier concepts can now be combined with control flow.

---

# Conditions With Dictionaries

I can also check whether a key exists in a dictionary.

```python
student = {
    "name": "Hanish",
    "age": 30
}

if "age" in student:
    print("Age information is available")
```

Output:

```text
Age information is available
```

Again, the `in` operator behaves according to the data structure I am working with.

---

# Truthy and Falsy Values

Python can evaluate values directly in a condition.

For example:

```python
name = "Hanish"

if name:
    print("A name was provided")
```

A non-empty string is treated as `True`.

An empty string is treated as `False`.

```python
name = ""

if name:
    print("A name was provided")
else:
    print("No name was provided")
```

Output:

```text
No name was provided
```

I am starting to see that Boolean logic in Python is broader than simply writing `True` and `False`.

---

# A Simple Input Example

Now I can combine several concepts from earlier topics.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")
```

Here the flow is:

```text
Input
  ↓
Type conversion
  ↓
Comparison
  ↓
Condition
  ↓
Output
```

This is the first time several concepts from the earlier sections are coming together into an actual decision-making program.

---

# A Practical Example

I can create a simple ticket-pricing program.

```python
age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age < 18:
    price = 100
else:
    price = 200

print(f"Ticket price: ₹{price}")
```

For example, if the user enters:

```text
12
```

the output is:

```text
Ticket price: ₹100
```

The program makes a decision based on the user's input.

---

# A Common Beginner Mistake

One mistake I need to watch for is confusing:

```python
=
```

with:

```python
==
```

`=` is used for **assignment**:

```python
age = 25
```

`==` is used for **comparison**:

```python
age == 25
```

For example:

```python
age = 25

if age == 25:
    print("Correct")
```

This distinction is important because the two operators have completely different purposes.

---

# Another Beginner Mistake: Condition Order

Consider:

```python
marks = 95

if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Excellent")
```

The output is:

```text
Pass
```

Why?

Because `95 >= 50` is already `True`, so Python never reaches the `elif`.

A better order is:

```python
marks = 95

if marks >= 90:
    print("Excellent")
elif marks >= 50:
    print("Pass")
```

Output:

```text
Excellent
```

This helped me understand that **the order of conditions matters**.

---

# What I Noticed

`if`, `elif`, and `else` changed the way I think about Python programs.

Earlier, I was mainly telling Python:

> "Do this."

Now I can tell Python:

> "If this is true, do this. Otherwise, try this."

That is an important step toward writing programs that respond differently depending on the data they receive.

---

# What Connected With Previous Topics?

### Variables

Conditions evaluate values stored in variables.

### Data Types

Different kinds of values can be used in conditions.

### Operators

Comparison and logical operators create conditions.

### Input

User input can determine which branch runs.

### Strings, Lists & Dictionaries

The `in` operator can be used with different data structures.

So control flow is not an isolated topic. It acts as a layer that allows me to make decisions using the concepts I have already learned.

---

# Practice

## Practice 1 — Positive, Negative or Zero

Create a number and determine whether it is:

* positive
* negative
* zero

---

## Practice 2 — Even or Odd

Ask the user for a number and determine whether it is even or odd.

Think about which operator you learned earlier can help.

---

## Practice 3 — Age Category

Ask the user for their age and classify it into suitable age groups.

Decide your own categories and conditions.

---

## Practice 4 — Grade Calculator

Ask the user for marks and assign a grade based on a range of scores.

Think carefully about the order of your conditions.

---

## Practice 5 — Login Check

Create a stored username and password.

Ask the user for their username and password and check whether both are correct.

---

## Practice 6 — Small Decision Program

Create a program that asks the user for a temperature.

Make the program display a different message depending on the temperature range.

Try solving these independently before looking at a solution.

---

## My Learning Note

> `if`, `elif`, and `else` were my first real introduction to decision-making in Python. I can now make a program behave differently depending on the data it receives. I also learned that condition order and indentation are just as important as the condition itself.

---
