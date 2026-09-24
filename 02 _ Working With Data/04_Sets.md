# Sets

A **set** is a Python data structure used to store a collection of **unique values**.

For example:

```python
fruits = {"apple", "banana", "mango"}
```

The most important thing I am learning about sets is that **duplicate values are automatically removed**.

Sets are also different from lists and tuples because I do not use them mainly for accessing values by position.

---

# Creating a Set

Sets are created using curly braces `{}`.

```python
fruits = {"apple", "banana", "mango"}

print(fruits)
```

A set contains unique values.

```python
numbers = {10, 20, 30, 10, 20}

print(numbers)
```

The duplicate values are removed, so the set contains each value only once.

> The order in which set elements are displayed should not be relied upon.

---

# Checking the Type

The data type of a set is `set`.

```python
numbers = {10, 20, 30}

print(type(numbers))
```

Output:

```text
<class 'set'>
```

---

# Creating an Empty Set

There is an important difference between `{}` and `set()`.

```python
empty = {}

print(type(empty))
```

This creates a **dictionary**, not a set.

To create an empty set:

```python
empty = set()

print(type(empty))
```

Output:

```text
<class 'set'>
```

This was an easy thing to confuse as a beginner.

---

# Duplicate Values

One of the main features of a set is that it stores only unique values.

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
```

Conceptually, the result contains:

```text
{1, 2, 3}
```

This makes sets useful when I need to remove duplicates from a collection.

---

# Sets Are Unordered

A set does not work like a list or tuple where I can rely on a particular positional order.

Because of this, I should not think of a set like:

```text
first item → index 0
second item → index 1
```

For example, this is not valid:

```python
numbers = {10, 20, 30}

# print(numbers[0])
```

Sets do not support indexing.

This is one of the biggest differences between:

**List / Tuple → ordered collection with indexing**

**Set → collection focused on unique values**

---

# Finding the Length

I can use `len()` to find how many unique values are in a set.

```python
numbers = {10, 20, 20, 30, 30}

print(len(numbers))
```

Output:

```text
3
```

The duplicates do not increase the length.

---

# Checking Whether a Value Exists

The `in` and `not in` operators work very naturally with sets.

```python
fruits = {"apple", "banana", "mango"}

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

This is one reason sets are useful when I mainly care about whether a value is present.

---

# Adding Values

Sets can be modified, so they are **mutable**.

I can add one value using `add()`.

```python
fruits = {"apple", "banana"}

fruits.add("mango")

print(fruits)
```

Now `"mango"` is part of the set.

If I add a value that already exists, the set remains unchanged.

```python
fruits.add("apple")

print(fruits)
```

There is still only one `"apple"`.

---

# Adding Multiple Values

I can use `update()` to add multiple values.

```python
fruits = {"apple", "banana"}

fruits.update(["mango", "orange"])

print(fruits)
```

The values from the other collection are added to the set.

`update()` can work with other iterables too.

---

# Removing Values

## `remove()`

`remove()` deletes a specified value.

```python
fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)
```

If the value does not exist, `remove()` raises a `KeyError`.

---

## `discard()`

`discard()` also removes a value, but it does **not** raise an error if the value is missing.

```python
fruits = {"apple", "banana", "mango"}

fruits.discard("orange")

print(fruits)
```

Nothing happens because `"orange"` is not in the set.

This difference is useful:

```text
remove()   → error if value is absent
discard()  → no error if value is absent
```

---

## `pop()`

`pop()` removes and returns an arbitrary element from the set.

```python
fruits = {"apple", "banana", "mango"}

removed = fruits.pop()

print(removed)
print(fruits)
```

Because sets are unordered, I should **not expect a particular value to be removed**.

---

## `clear()`

`clear()` removes all values.

```python
fruits = {"apple", "banana", "mango"}

fruits.clear()

print(fruits)
```

Output:

```text
set()
```

---

# Set Operations

This is where sets become especially interesting.

Python allows me to perform mathematical-style operations between sets.

Suppose:

```python
python_students = {"A", "B", "C", "D"}
sql_students = {"C", "D", "E", "F"}
```

Some students are learning both Python and SQL.

---

## Union

A **union** combines all unique values from both sets.

```python
python_students = {"A", "B", "C", "D"}
sql_students = {"C", "D", "E", "F"}

all_students = python_students | sql_students

print(all_students)
```

The result contains:

```text
{"A", "B", "C", "D", "E", "F"}
```

I can also use the `.union()` method:

```python
all_students = python_students.union(sql_students)
```

---

## Intersection

An **intersection** contains values that exist in both sets.

```python
python_students = {"A", "B", "C", "D"}
sql_students = {"C", "D", "E", "F"}

both = python_students & sql_students

print(both)
```

Result:

```text
{"C", "D"}
```

I can also use:

```python
both = python_students.intersection(sql_students)
```

---

## Difference

The **difference** returns values that exist in one set but not the other.

```python
python_students = {"A", "B", "C", "D"}
sql_students = {"C", "D", "E", "F"}

only_python = python_students - sql_students

print(only_python)
```

Result:

```text
{"A", "B"}
```

The direction matters.

```python
only_sql = sql_students - python_students

print(only_sql)
```

Result:

```text
{"E", "F"}
```

---

## Symmetric Difference

Symmetric difference gives values that are in either set, but **not in both**.

```python
python_students = {"A", "B", "C", "D"}
sql_students = {"C", "D", "E", "F"}

different = python_students ^ sql_students

print(different)
```

Result:

```text
{"A", "B", "E", "F"}
```

The `.symmetric_difference()` method does the same thing.

---

# Comparing Sets

Sets can also be compared to understand relationships between them.

## Subset

A set is a subset if all of its values exist inside another set.

```python
numbers = {1, 2, 3, 4, 5}
small_numbers = {1, 2, 3}

print(small_numbers.issubset(numbers))
```

Output:

```text
True
```

---

## Superset

A superset contains all the values of another set.

```python
numbers = {1, 2, 3, 4, 5}
small_numbers = {1, 2, 3}

print(numbers.issuperset(small_numbers))
```

Output:

```text
True
```

---

## Disjoint Sets

Two sets are disjoint when they have no common values.

```python
set_a = {1, 2, 3}
set_b = {4, 5, 6}

print(set_a.isdisjoint(set_b))
```

Output:

```text
True
```

---

# Converting a List to a Set

One practical use of sets is removing duplicates from a list.

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)
```

The result contains only unique values.

I can convert it back into a list:

```python
unique_numbers = list(set(numbers))

print(unique_numbers)
```

One thing to remember is that converting through a set does not preserve the original order.

---

# Set Methods I Have Learned

| Method                   | Purpose                                      |
| ------------------------ | -------------------------------------------- |
| `add()`                  | Add one value                                |
| `update()`               | Add multiple values                          |
| `remove()`               | Remove a value and raise an error if absent  |
| `discard()`              | Remove a value without error if absent       |
| `pop()`                  | Remove and return an arbitrary element       |
| `clear()`                | Remove all values                            |
| `union()`                | Combine unique values                        |
| `intersection()`         | Find common values                           |
| `difference()`           | Find values only in one set                  |
| `symmetric_difference()` | Find values in either set but not both       |
| `issubset()`             | Check whether a set is contained in another  |
| `issuperset()`           | Check whether a set contains another         |
| `isdisjoint()`           | Check whether two sets have no common values |

---

# Sets vs Lists vs Tuples

Now I can start comparing the three data structures I have learned so far.

| Feature         | List                 | Tuple            | Set                 |
| --------------- | -------------------- | ---------------- | ------------------- |
| Ordered         | Yes                  | Yes              | No guaranteed order |
| Mutable         | Yes                  | No               | Yes                 |
| Duplicates      | Allowed              | Allowed          | Not stored          |
| Indexing        | Yes                  | Yes              | No                  |
| Slicing         | Yes                  | Yes              | No                  |
| `in` / `not in` | Yes                  | Yes              | Yes                 |
| Main idea       | Collection of values | Fixed collection | Unique values       |

This comparison is becoming important because I am starting to understand that different data structures are useful for different situations.

---

# A Small Practical Example

Imagine I collected names from two different classes.

```python
class_a = {"Hanish", "Rahul", "Aman", "Priya"}
class_b = {"Priya", "Aman", "Riya", "Karan"}
```

I can find:

### All students

```python
all_students = class_a | class_b
```

### Students in both classes

```python
both_classes = class_a & class_b
```

### Students only in Class A

```python
only_a = class_a - class_b
```

This is where the mathematical idea behind sets starts becoming practical.

---

# What I Noticed

Sets changed the way I think about collections.

With lists and tuples, I was often thinking about:

> "Where is this value?"

With sets, I am more likely to think:

> "Does this value exist?"
> "Is this value unique?"
> "What values do these two collections have in common?"

The set operations also introduced a more mathematical way of working with data.

---

# What Connected With Previous Topics?

### Lists

I can convert a list into a set to remove duplicates.

### Tuples

Both can store multiple values, but tuples preserve order while sets focus on uniqueness.

### Operators

I have now seen operators such as:

```python
|
&
-
^
```

used specifically for set operations.

### `in`

The membership operator I learned earlier is especially useful with sets.

This is helping me see how Python's existing concepts keep getting reused in new ways.

---

# Practice

## Practice 1 — Remove Duplicates

Create a list with repeated numbers.

Convert it into a set and observe the result.

---

## Practice 2 — Add & Remove

Create a set of five fruits.

Then:

* add a new fruit
* remove one fruit
* check whether a specific fruit exists

---

## Practice 3 — Union & Intersection

Create two sets of numbers.

Find:

* all unique numbers
* numbers present in both sets

---

## Practice 4 — Difference

Create two sets representing two groups of students.

Find the students who are only in the first group.

---

## Practice 5 — Think About the Data Structure

Which would you choose?

**A:** A shopping cart where duplicate items may matter.

**B:** A collection of unique user IDs.

**C:** A fixed pair of coordinates.

Think about whether a **list, set, or tuple** makes the most sense and explain why.

---

## My Learning Note

> Sets introduced me to the idea that a data structure can be chosen based on what I need from the data. If uniqueness matters more than position, a set can be much more useful than a list or tuple.

---

