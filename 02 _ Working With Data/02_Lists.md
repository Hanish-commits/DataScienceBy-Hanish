# Lists

A **list** is a Python data type used to store multiple values in a single variable.

Unlike a string, which stores a sequence of characters, a list can store different kinds of values.

```python
fruits = ["apple", "banana", "mango"]
```

A list is one of the most commonly used Python data structures, so I need to become comfortable creating, accessing, and modifying lists.

---

# Creating a List

Lists are created using square brackets `[]`.

```python
fruits = ["apple", "banana", "mango"]

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

An empty list can also be created:

```python
items = []

print(items)
```

---

# Lists Can Store Different Data Types

A list does not have to contain only one type of value.

```python
student = ["Hanish", 30, 5.9, True]

print(student)
```

The list contains:

* a string
* an integer
* a float
* a Boolean

In real programs, lists often contain values of the same general kind, but Python allows mixed data too.

---

# Lists Are Ordered

The values in a list have a specific order.

```python
fruits = ["apple", "banana", "mango"]
```

The positions are:

```text
apple    → 0
banana   → 1
mango    → 2
```

This means I can access individual values using indexes.

---

# List Indexing

Lists use **zero-based indexing**, just like strings.

```python
fruits = ["apple", "banana", "mango"]

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

I can also use negative indexing.

```python
print(fruits[-1])
print(fruits[-2])
```

Output:

```text
mango
banana
```

---

# List Slicing

Lists can also be sliced.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
```

Output:

```text
[10, 20, 30]
```

Just like strings, the start index is included and the stop index is excluded.

I can also use other slicing patterns:

```python
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])
```

Output:

```text
[10, 20, 30]
[30, 40, 50]
[10, 30, 50]
[50, 40, 30, 20, 10]
```

---

# Lists Are Mutable

One of the biggest differences between strings and lists is that **lists are mutable**.

This means I can change an individual item after creating the list.

```python
fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)
```

Output:

```text
['apple', 'orange', 'mango']
```

The existing list was changed.

This is different from strings, which are immutable.

---

# Finding the Length of a List

I can use `len()` to find the number of items in a list.

```python
fruits = ["apple", "banana", "mango"]

print(len(fruits))
```

Output:

```text
3
```

---

# Adding Items

Python provides several ways to add items to a list.

## `append()`

`append()` adds one item to the **end** of the list.

```python
fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

---

## `insert()`

`insert()` adds an item at a specific position.

```python
fruits = ["apple", "mango"]

fruits.insert(1, "banana")

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

The first argument is the index where the item should be inserted.

---

## `extend()`

`extend()` adds multiple items from another iterable to the end of the list.

For example:

```python
fruits = ["apple", "banana"]

fruits.extend(["mango", "orange"])

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango', 'orange']
```

This is different from `append()`.

```python
fruits = ["apple", "banana"]

fruits.append(["mango", "orange"])

print(fruits)
```

Output:

```text
['apple', 'banana', ['mango', 'orange']]
```

`append()` adds the entire object as one item, while `extend()` adds its elements individually.

This difference is important.

---

# Removing Items

## `remove()`

`remove()` removes the first matching value.

```python
fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)
```

Output:

```text
['apple', 'mango']
```

If the value is not present, Python raises a `ValueError`.

---

## `pop()`

`pop()` removes an item using its index and returns the removed value.

```python
fruits = ["apple", "banana", "mango"]

removed_item = fruits.pop(1)

print(removed_item)
print(fruits)
```

Output:

```text
banana
['apple', 'mango']
```

If no index is provided, `pop()` removes the last item.

```python
fruits = ["apple", "banana", "mango"]

removed_item = fruits.pop()

print(removed_item)
print(fruits)
```

Output:

```text
mango
['apple', 'banana']
```

---

## `del`

I can also use `del` to remove an item by index.

```python
fruits = ["apple", "banana", "mango"]

del fruits[1]

print(fruits)
```

Output:

```text
['apple', 'mango']
```

---

# Clearing a List

`clear()` removes all items from a list.

```python
fruits = ["apple", "banana", "mango"]

fruits.clear()

print(fruits)
```

Output:

```text
[]
```

The list still exists, but it is now empty.

---

# Checking Whether an Item Exists

Just like with strings, I can use `in` and `not in`.

```python
fruits = ["apple", "banana", "mango"]

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

# Finding the Position of an Item

`index()` returns the position of the first matching item.

```python
fruits = ["apple", "banana", "mango"]

print(fruits.index("banana"))
```

Output:

```text
1
```

---

# Counting Items

`count()` tells me how many times a value appears.

```python
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```

Output:

```text
3
```

This will become especially useful later when I start processing collections of data.

---

# Sorting a List

The `sort()` method sorts the items in place.

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

I can also sort in descending order.

```python
numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

For now, I am using sorting with numbers. Sorting strings also has its own behavior, which I can explore as I practice.

---

# Reversing a List

`reverse()` reverses the current order of the list.

```python
fruits = ["apple", "banana", "mango"]

fruits.reverse()

print(fruits)
```

Output:

```text
['mango', 'banana', 'apple']
```

This is different from `sort(reverse=True)`.

* `reverse()` → reverses the current order
* `sort(reverse=True)` → sorts the values in descending order

---

# Copying a List

I can create a separate copy using `copy()`.

```python
fruits = ["apple", "banana", "mango"]

new_fruits = fruits.copy()

print(new_fruits)
```

This is useful when I want another list without simply referring to the same list object.

---

# A Common Beginner Problem

Consider:

```python
fruits = ["apple", "banana", "mango"]

new_fruits = fruits

new_fruits.append("orange")

print(fruits)
```

The output is:

```text
['apple', 'banana', 'mango', 'orange']
```

At first, this can be confusing because I only changed `new_fruits`.

The reason is that both variables refer to the same list.

Using `copy()` creates a separate list:

```python
fruits = ["apple", "banana", "mango"]

new_fruits = fruits.copy()

new_fruits.append("orange")

print(fruits)
print(new_fruits)
```

Output:

```text
['apple', 'banana', 'mango']
['apple', 'banana', 'mango', 'orange']
```

This is an important thing to understand before working with larger programs.

---

# Lists Inside Lists

A list can contain another list.

```python
numbers = [
    [1, 2, 3],
    [4, 5, 6]
]

print(numbers)
```

This is called a **nested list**.

I can access an inner value using multiple indexes:

```python
print(numbers[0][1])
```

Output:

```text
2
```

I will explore nested data more as my Python skills develop.

---

# List Methods I Have Learned

| Method      | Purpose                         |
| ----------- | ------------------------------- |
| `append()`  | Add one item to the end         |
| `insert()`  | Add an item at a specific index |
| `extend()`  | Add multiple items              |
| `remove()`  | Remove the first matching value |
| `pop()`     | Remove and return an item       |
| `clear()`   | Remove all items                |
| `index()`   | Find the position of an item    |
| `count()`   | Count occurrences               |
| `sort()`    | Sort the list                   |
| `reverse()` | Reverse the current order       |
| `copy()`    | Create a copy                   |

---

# What I Noticed

Lists feel like a bigger step from strings.

With a string, I was mainly working with **characters**.

With a list, I can store multiple values and then:

**Access → Change → Add → Remove → Search → Sort**

The biggest new idea for me is **mutability**.

Strings cannot have individual characters changed directly, but lists can have individual items changed.

---

# What Connected With Previous Topics?

Lists build directly on concepts I already learned.

### Variables

A list can be stored in a variable.

### Data Types

A list has the type `list`.

### Indexing & Slicing

The same ideas I learned with strings also work with lists.

### Operators

`in` and `not in` can check whether an item exists.

### Methods

Lists have their own methods for modifying and working with data.

This is helping me see that Python concepts are not isolated. The same ideas often appear again with different data structures.

---

# Practice

## Practice 1 — Create a List

Create a list containing five foods you like.

Print:

* the complete list
* the first item
* the last item
* the length of the list

---

## Practice 2 — Modify a List

Create:

```python
numbers = [10, 20, 30, 40, 50]
```

Then:

* change `30` to `35`
* add `60`
* remove `20`

Print the final list.

---

## Practice 3 — Experiment With `append()` and `extend()`

Create a list and try both:

```python
append()
extend()
```

Observe how the resulting lists differ.

---

## Practice 4 — Sorting

Create an unsorted list of numbers.

Sort it:

1. in ascending order
2. in descending order

---

## Practice 5 — Search & Count

Create a list containing repeated values.

Use:

* `in`
* `index()`
* `count()`

to explore the list.

---

## Practice 6 — Small Application

Create a list representing items in a shopping cart.

Add an item, remove an item, check whether a specific item exists, and print the final cart.

Try solving these yourself before looking for solutions.

---

# My Learning Note

> Lists helped me understand how Python can store multiple pieces of data together and work with them as a collection. I also learned that lists are mutable, which makes them very different from strings.

---



