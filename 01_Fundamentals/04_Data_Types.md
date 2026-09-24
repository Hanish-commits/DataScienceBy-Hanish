# Data Types

In the previous topic, I learned how variables can store values.

But not all values are the same.

For example:

```python
name = "Hanish"
age = 30
height = 5.9
is_learning = True
```

Here, each variable contains a different kind of value.

These different kinds of values are called **data types**.

---

## Why Do Data Types Matter?

Python needs to know what kind of data it is working with because different types of data behave differently.

For example:

```python
age = 30
```

Here, `age` contains a number, so I can perform mathematical operations on it.

But:

```python
name = "Hanish"
```

contains text, so I would work with it differently.

Understanding data types helps me know:

* what kind of value I am working with
* what operations I can perform
* how Python treats that value
* why some operations work while others produce errors

---

# Common Python Data Types

At this stage, the main data types I am learning are:

| Data Type | Example    | Used For          |
| --------- | ---------- | ----------------- |
| `str`     | `"Python"` | Text              |
| `int`     | `25`       | Whole numbers     |
| `float`   | `5.9`      | Decimal numbers   |
| `bool`    | `True`     | True/False values |

Python has many more built-in data types, which I will learn as I progress.

---

## 1. String (`str`)

A string represents text.

```python
name = "Hanish"
message = "I am learning Python"
```

Strings are written inside quotes.

```python
print(name)
print(message)
```

### Output

```text
Hanish
I am learning Python
```

I will explore strings in much more detail in the **Strings** section later.

---

## 2. Integer (`int`)

An integer is a whole number without a decimal part.

```python
age = 30
score = 100
temperature = -5
```

Integers can be positive, negative, or zero.

They can also be used in mathematical operations.

```python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
```

### Output

```text
15
5
50
```

---

## 3. Float (`float`)

A float represents a number that contains a decimal value.

```python
height = 5.9
price = 99.50
temperature = 36.5
```

For example:

```python
price = 99.50
quantity = 2

total = price * quantity

print(total)
```

### Output

```text
199.0
```

---

## 4. Boolean (`bool`)

A Boolean represents one of two values:

```python
True
False
```

For example:

```python
is_learning = True
is_finished = False

print(is_learning)
print(is_finished)
```

### Output

```text
True
False
```

Booleans become especially important when working with conditions and decision-making.

---

# Finding the Data Type

Python provides the `type()` function to check the type of a value.

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

### Output

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

This is useful when I am unsure what kind of value a variable contains.

---

# One Variable, Different Values

A variable can be assigned a new value later.

For example:

```python
value = 10
print(type(value))

value = "Python"
print(type(value))
```

### Output

```text
<class 'int'>
<class 'str'>
```

The value changed from an integer to a string.

This is one of the things I am beginning to notice about Python's dynamic typing.

---

# A Simple Experiment

I can compare how different data types behave.

```python
number = 10
text = "10"

print(number + 5)
print(text + "5")
```

### Output

```text
15
105
```

The first operation performs numerical addition.

The second joins two strings together.

This shows why understanding the **type of a value** matters.

---

# What I Noticed

At first, variables and data types can feel like two separate concepts.

Now I am starting to see the connection:

**Variable → stores a value → the value has a data type**

For example:

```python
age = 30
```

* `age` → variable
* `30` → value
* `int` → data type

Understanding this relationship will be important as I start working with more complex Python programs.

---

# Practice

### Practice 1

Create one variable for each of these:

* your name
* your age
* your height
* whether you are currently learning Python

Then use `type()` to check each one.

### Practice 2

Create:

```python
number = 25
text = "25"
```

Use `type()` to find out how they are different.

### Practice 3

Create a variable called `value`.

Assign it an integer, check its type, then assign it a string and check its type again.

Try these yourself before looking at a solution.

---

## My Learning Note

> Data types helped me understand that Python doesn't just store values — different values behave differently depending on their type. I want to get comfortable recognizing the type of data I am working with before moving to more complex concepts.

---
