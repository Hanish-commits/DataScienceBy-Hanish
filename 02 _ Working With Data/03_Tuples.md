# Tuples

A **tuple** is a Python data structure used to store multiple values in a single variable.

At first glance, tuples look very similar to lists.

```python
fruits = ("apple", "banana", "mango")
```

The major difference I am learning is that **tuples are immutable**.

That means once a tuple is created, its individual elements cannot be changed directly.

---

# Creating a Tuple

Tuples are commonly created using parentheses `()`.

```python
fruits = ("apple", "banana", "mango")

print(fruits)
```

Output:

```text
('apple', 'banana', 'mango')
```

An empty tuple can be created with:

```python
items = ()

print(items)
```

---

# Checking the Type

A tuple has the data type `tuple`.

```python
numbers = (10, 20, 30)

print(type(numbers))
```

Output:

```text
<class 'tuple'>
```

---

# Creating a Tuple Without Parentheses

Python also allows tuple packing without explicitly writing parentheses.

```python
numbers = 10, 20, 30

print(numbers)
print(type(numbers))
```

Output:

```text
(10, 20, 30)
<class 'tuple'>
```

The parentheses are often used because they make the intention clearer.

---

# The Single-Item Tuple

There is an important detail when creating a tuple with only one item.

This is **not** a tuple:

```python
number = (10)

print(type(number))
```

It is an integer.

To create a one-item tuple, I need a comma:

```python
number = (10,)

print(type(number))
```

Output:

```text
<class 'tuple'>
```

The comma is what makes it a tuple.

---

# Tuples Can Contain Different Data Types

Just like lists, tuples can contain different types of values.

```python
student = ("Hanish", 30, 5.9, True)

print(student)
```

A tuple can contain:

* strings
* integers
* floats
* Booleans
* other objects

---

# Tuple Indexing

Tuples are ordered, so I can access individual items using indexes.

```python
fruits = ("apple", "banana", "mango")

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Output:

```text
apple
banana
mango
```

Tuples use **zero-based indexing**, just like strings and lists.

---

# Negative Indexing

Negative indexes work with tuples too.

```python
fruits = ("apple", "banana", "mango")

print(fruits[-1])
print(fruits[-2])
```

Output:

```text
mango
banana
```

---

# Tuple Slicing

Tuples can also be sliced.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[0:3])
print(numbers[2:])
print(numbers[::-1])
```

Output:

```text
(10, 20, 30)
(30, 40, 50)
(50, 40, 30, 20, 10)
```

The slicing rules are the same as the ones I learned with strings and lists.

---

# Tuples Are Immutable

This is the most important concept in this topic.

Once a tuple is created, I cannot directly change one of its elements.

For example:

```python
fruits = ("apple", "banana", "mango")

fruits[1] = "orange"
```

This produces a `TypeError`.

Unlike a list:

```python
fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)
```

a tuple does not allow this kind of modification.

This is the key difference:

```text
List   → Mutable
Tuple  → Immutable
```

---

# Adding and Removing Items

Tuples do not have methods such as:

```python
append()
remove()
pop()
```

because the tuple itself cannot be changed.

For example, this does not work:

```python
numbers = (10, 20, 30)

numbers.append(40)
```

Python raises an `AttributeError` because tuples do not provide `append()`.

---

# Finding the Length

I can use `len()` with tuples.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

Output:

```text
4
```

---

# Checking Whether an Item Exists

The `in` and `not in` operators also work with tuples.

```python
fruits = ("apple", "banana", "mango")

print("banana" in fruits)
print("orange" in fruits)
print("orange" not in fruits)
```

Output:

```text
True
False
True
```

---

# Tuple Methods

Tuples have fewer methods than lists because they cannot be modified.

The two main methods I need to know are:

### `count()`

Counts how many times a value appears.

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

Output:

```text
3
```

### `index()`

Returns the position of the first matching value.

```python
fruits = ("apple", "banana", "mango")

print(fruits.index("banana"))
```

Output:

```text
1
```

---

# Tuple Packing

I can put multiple values into a tuple.

```python
student = ("Hanish", 30, "Data Science")

print(student)
```

This is called **tuple packing**.

---

# Tuple Unpacking

I can also assign the values from a tuple to separate variables.

```python
student = ("Hanish", 30, "Data Science")

name, age, course = student

print(name)
print(age)
print(course)
```

Output:

```text
Hanish
30
Data Science
```

The number of variables needs to match the number of values being unpacked.

This is a useful Python feature that I will see again later.

---

# Converting Between Lists and Tuples

I can convert a list into a tuple using `tuple()`.

```python
fruits = ["apple", "banana", "mango"]

fruits_tuple = tuple(fruits)

print(fruits_tuple)
print(type(fruits_tuple))
```

Output:

```text
('apple', 'banana', 'mango')
<class 'tuple'>
```

I can also convert a tuple into a list using `list()`.

```python
fruits = ("apple", "banana", "mango")

fruits_list = list(fruits)

print(fruits_list)
print(type(fruits_list))
```

This can be useful when I need to work with the same data but require a different type.

---

# Lists vs Tuples

The biggest differences I have learned are:

| Feature         | List | Tuple |
| --------------- | ---- | ----- |
| Syntax          | `[]` | `()`  |
| Ordered         | Yes  | Yes   |
| Mutable         | Yes  | No    |
| Indexing        | Yes  | Yes   |
| Slicing         | Yes  | Yes   |
| `in` / `not in` | Yes  | Yes   |
| `append()`      | Yes  | No    |
| `remove()`      | Yes  | No    |
| `pop()`         | Yes  | No    |
| `count()`       | Yes  | Yes   |
| `index()`       | Yes  | Yes   |

The most important distinction for me is:

**List → when I need a collection I may change**

**Tuple → when I want a collection that should remain unchanged**

---

# When Would I Use a Tuple?

I would use a tuple when the collection of values should remain fixed.

For example:

```python
coordinates = (12.9716, 77.5946)
```

The values represent a fixed pair of coordinates.

Another example:

```python
rgb = (255, 255, 255)
```

The exact use case depends on the program, but the idea is that a tuple can communicate:

> "These values belong together, and I don't expect to modify this collection."

---

# What I Noticed

At first, tuples seemed almost identical to lists.

The difference became clear when I tried to modify one of their elements.

This helped me understand that choosing a data structure is not only about how the data looks. It is also about **what I need to do with that data**.

If I need to modify the collection, a list may be appropriate.

If the collection should remain unchanged, a tuple may be more appropriate.

---

# What Connected With Previous Topics?

Tuples reuse several concepts I already learned.

### Indexing

Just like strings and lists, tuples use zero-based indexing.

### Slicing

The same slicing rules apply.

### `len()`

I can find the number of items.

### `in`

I can check whether a value exists.

### Type Conversion

I can convert between lists and tuples using `list()` and `tuple()`.

This is making the different Python data structures easier to compare.

---

# Practice

## Practice 1 — Create a Tuple

Create a tuple containing:

* your name
* your age
* your city

Print the tuple and its type.

---

## Practice 2 — Indexing

Using:

```python
numbers = (10, 20, 30, 40, 50)
```

print:

* the first value
* the last value
* the third value

---

## Practice 3 — Slicing

Using the same tuple, print:

* the first three values
* the last three values
* the reversed tuple

---

## Practice 4 — Unpacking

Create a tuple containing three values and unpack them into three separate variables.

---

## Practice 5 — List to Tuple

Create a list of five items and convert it into a tuple.

Check the type before and after conversion.

---

## Practice 6 — Think About the Difference

Consider these two situations:

**Situation A:** A shopping cart where items can be added and removed.

**Situation B:** A fixed set of coordinates.

Decide whether a **list** or **tuple** makes more sense for each situation and explain why.

---

## My Learning Note

> Tuples helped me understand the idea of immutability more clearly. They look a lot like lists, but the fact that I cannot directly change their contents makes them useful for situations where data should stay fixed.

---

## Next Step

