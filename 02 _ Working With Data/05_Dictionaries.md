# Dictionaries

A **dictionary** is a Python data structure used to store data as **key-value pairs**.

Instead of accessing a value by its position, I access it using a key.

For example:

```python
student = {
    "name": "Hanish",
    "age": 30,
    "course": "Data Science"
}
```

Here:

* `"name"` → key
* `"Hanish"` → value
* `"age"` → key
* `30` → value

The key identifies the value associated with it.

---

# Creating a Dictionary

Dictionaries are created using curly braces `{}`.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "course": "Data Science"
}

print(student)
```

Output:

```text
{'name': 'Hanish', 'age': 30, 'course': 'Data Science'}
```

An empty dictionary can be created with:

```python
student = {}

print(student)
```

Its type is:

```python
print(type(student))
```

Output:

```text
<class 'dict'>
```

---

# Key-Value Pairs

A dictionary stores information in this form:

```text
key → value
```

For example:

```python
person = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}
```

I can think of it as:

```text
"name" → "Hanish"
"age"  → 30
"city" → "Bengaluru"
```

This makes dictionaries useful when the relationship between a label and its value matters.

---

# Accessing Values

I can access a dictionary value using its key.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "course": "Data Science"
}

print(student["name"])
print(student["age"])
```

Output:

```text
Hanish
30
```

Unlike lists and tuples, I am not using an index such as `0` or `1`.

I am using the key itself.

---

# Using `get()`

Another way to access a value is the `get()` method.

```python
student = {
    "name": "Hanish",
    "age": 30
}

print(student.get("name"))
```

Output:

```text
Hanish
```

One useful difference is what happens when the key does not exist.

Using:

```python
print(student["city"])
```

produces a `KeyError`.

But:

```python
print(student.get("city"))
```

returns:

```text
None
```

I can also provide a default value:

```python
print(student.get("city", "Not available"))
```

Output:

```text
Not available
```

---

# Adding a New Key-Value Pair

I can add a new item by assigning a value to a new key.

```python
student = {
    "name": "Hanish",
    "age": 30
}

student["city"] = "Bengaluru"

print(student)
```

Output:

```text
{'name': 'Hanish', 'age': 30, 'city': 'Bengaluru'}
```

---

# Updating a Value

I can change the value associated with an existing key.

```python
student = {
    "name": "Hanish",
    "age": 30
}

student["age"] = 31

print(student)
```

Output:

```text
{'name': 'Hanish', 'age': 31}
```

The key stays the same, but its value changes.

---

# Dictionaries Are Mutable

Like lists and sets, dictionaries are **mutable**.

That means I can add, remove, and change their contents after creating them.

For example:

```python
student = {
    "name": "Hanish",
    "age": 30
}

student["age"] = 31
student["city"] = "Bengaluru"

print(student)
```

The original dictionary has been modified.

---

# Removing Items

## `pop()`

`pop()` removes a specific key and returns its value.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

removed = student.pop("age")

print(removed)
print(student)
```

Output:

```text
30
{'name': 'Hanish', 'city': 'Bengaluru'}
```

---

## `popitem()`

`popitem()` removes and returns the last inserted key-value pair.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

removed = student.popitem()

print(removed)
print(student)
```

Output:

```text
('city', 'Bengaluru')
{'name': 'Hanish', 'age': 30}
```

---

## `del`

I can also delete a specific key using `del`.

```python
student = {
    "name": "Hanish",
    "age": 30
}

del student["age"]

print(student)
```

---

## `clear()`

`clear()` removes all key-value pairs.

```python
student = {
    "name": "Hanish",
    "age": 30
}

student.clear()

print(student)
```

Output:

```text
{}
```

---

# Checking Whether a Key Exists

The `in` operator works with dictionaries.

```python
student = {
    "name": "Hanish",
    "age": 30
}

print("name" in student)
print("city" in student)
```

Output:

```text
True
False
```

When used directly with a dictionary, `in` checks the **keys**.

```python
print("Hanish" in student)
```

This is `False` because `"Hanish"` is a value, not a key.

---

# Getting Dictionary Keys

The `keys()` method gives me a view of the dictionary's keys.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

print(student.keys())
```

I can convert it into a list if I need one:

```python
print(list(student.keys()))
```

---

# Getting Dictionary Values

The `values()` method gives me the values.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

print(student.values())
print(list(student.values()))
```

---

# Getting Keys and Values Together

The `items()` method gives me key-value pairs.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

print(student.items())
```

Each item is represented as a key-value pair.

For example, conceptually:

```text
("name", "Hanish")
("age", 30)
("city", "Bengaluru")
```

I will use `items()` much more when I learn loops.

---

# Updating a Dictionary

The `update()` method can add new key-value pairs or update existing ones.

```python
student = {
    "name": "Hanish",
    "age": 30
}

student.update({
    "age": 31,
    "city": "Bengaluru"
})

print(student)
```

Output:

```text
{'name': 'Hanish', 'age': 31, 'city': 'Bengaluru'}
```

The existing `age` value was updated, and `city` was added.

---

# Dictionary Keys Must Be Unique

A dictionary cannot have two separate entries with the same key.

For example:

```python
student = {
    "name": "Hanish",
    "name": "Rahul"
}

print(student)
```

The later value replaces the earlier one.

The result is:

```text
{'name': 'Rahul'}
```

This is an important difference from collections such as lists, where duplicate values are allowed.

---

# Values Can Be Duplicated

While keys must be unique, different keys can have the same value.

```python
students = {
    "student_1": "Python",
    "student_2": "Python",
    "student_3": "SQL"
}

print(students)
```

There is no problem with `"Python"` appearing more than once as a value.

---

# Different Data Types as Values

Dictionary values can contain different data types.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "height": 5.9,
    "is_learning": True
}

print(student)
```

This is similar to what I saw with lists and tuples.

---

# Lists Inside Dictionaries

A dictionary value can also be another data structure.

```python
student = {
    "name": "Hanish",
    "skills": ["Python", "SQL", "Excel"]
}

print(student["skills"])
```

Output:

```text
['Python', 'SQL', 'Excel']
```

I can then access an individual list item:

```python
print(student["skills"][0])
```

Output:

```text
Python
```

This shows how Python data structures can be combined.

---

# Dictionaries Inside Dictionaries

A dictionary can also contain another dictionary.

```python
student = {
    "name": "Hanish",
    "details": {
        "age": 30,
        "city": "Bengaluru"
    }
}

print(student["details"]["city"])
```

Output:

```text
Bengaluru
```

This is called a **nested dictionary**.

Nested structures will become very important later when I work with more complex data.

---

# Dictionary Length

I can use `len()` to find the number of key-value pairs.

```python
student = {
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}

print(len(student))
```

Output:

```text
3
```

The length represents the number of keys.

---

# A Small Practical Example

Suppose I want to store information about a product.

```python
product = {
    "name": "Laptop",
    "price": 75000,
    "quantity": 2
}
```

I can calculate the total value:

```python
total = product["price"] * product["quantity"]

print(total)
```

Output:

```text
150000
```

Now the dictionary is not just storing information. I am using that structured information in a calculation.

This is starting to look more like the kind of structured data I will work with later.

---

# Why Dictionaries Matter for Data Science

Dictionaries are especially useful because many real-world data formats use **key-value structures**.

For example, data from an API or a JSON file often looks conceptually like:

```python
{
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}
```

Later, when I work with APIs, JSON, Pandas, and other Data Science tools, I will see this structure repeatedly.

For now, I want to understand the Python dictionary itself before moving to those tools.

---

# Dictionary Methods I Have Learned

| Method      | Purpose                       |
| ----------- | ----------------------------- |
| `get()`     | Access a value safely         |
| `keys()`    | Get dictionary keys           |
| `values()`  | Get dictionary values         |
| `items()`   | Get key-value pairs           |
| `update()`  | Add or update multiple pairs  |
| `pop()`     | Remove a specific key         |
| `popitem()` | Remove the last inserted pair |
| `clear()`   | Remove all pairs              |

---

# Dictionaries vs Other Data Structures

I can now compare the four main data structures I have learned.

| Feature    | List       | Tuple            | Set                 | Dictionary             |
| ---------- | ---------- | ---------------- | ------------------- | ---------------------- |
| Ordered    | Yes        | Yes              | No guaranteed order | Yes, insertion order   |
| Mutable    | Yes        | No               | Yes                 | Yes                    |
| Duplicates | Allowed    | Allowed          | Not stored          | Keys must be unique    |
| Indexing   | Yes        | Yes              | No                  | No positional indexing |
| Main idea  | Collection | Fixed collection | Unique values       | Key-value pairs        |

The biggest idea for me here is:

**List → values by position**

**Tuple → fixed values by position**

**Set → unique values**

**Dictionary → values identified by keys**

---

# What I Noticed

Dictionaries feel different from the other data structures because I am no longer mainly asking:

> "What is at position 0?"

Instead, I am asking:

> "What value belongs to this key?"

That makes dictionaries a natural way to represent information where each value has a label.

I also noticed that Python data structures can be combined. A dictionary can contain lists, and dictionaries can even contain other dictionaries.

---

# What Connected With Previous Topics?

### Variables

I can store a dictionary in a variable.

### Data Types

The type of a dictionary is `dict`.

### Lists & Tuples

Dictionaries can contain lists and tuples as values.

### Sets

Dictionaries use curly braces too, which initially confused me. The presence of `key: value` pairs distinguishes a dictionary from a set.

### `in`

Membership testing works with dictionary keys.

### Type Conversion

I can convert some other data structures into dictionaries when the data has the appropriate structure.

---

# Practice

## Practice 1 — Student Dictionary

Create a dictionary containing:

* name
* age
* city
* course

Print each value using its key.

---

## Practice 2 — Modify the Dictionary

Using your dictionary:

* change one value
* add a new key-value pair
* remove one key

Print the final dictionary.

---

## Practice 3 — Explore Dictionary Methods

Create a dictionary and experiment with:

```python
keys()
values()
items()
get()
```

Observe what each one returns.

---

## Practice 4 — Nested Data

Create a dictionary where one key contains a list of three skills.

Access:

* the complete list
* the first skill

---

## Practice 5 — Product Example

Create a product dictionary containing:

* product name
* price
* quantity

Calculate the total value using the dictionary values.

---

## Practice 6 — Choose the Data Structure

Think about which structure makes sense:

**A:** A collection of unique email addresses

**B:** A student's information where each piece of data has a label

**C:** A shopping list where order matters

**D:** A fixed pair of coordinates

Choose between:

**List / Tuple / Set / Dictionary**

and explain your reasoning.

---

## My Learning Note

> Dictionaries helped me understand another way of organizing data. Instead of relying on position, I can give each value a meaningful key. I can already see why this structure will be useful later when I work with structured data.

---