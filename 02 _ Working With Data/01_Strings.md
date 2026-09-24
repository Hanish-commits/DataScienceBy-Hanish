# Strings

Strings are used to store and work with **text** in Python.

I first encountered strings while learning data types, but this topic goes much deeper. Strings have their own operations and methods that allow me to access, search, modify, and format text.

Text is also extremely important in Data Science because real-world data often contains names, categories, descriptions, addresses, labels, and other textual information.

---

# Creating Strings

A string is created by putting text inside quotes.

```python
name = "Hanish"
city = 'Bengaluru'
```

Python allows both single and double quotes.

```python
text1 = "Hello Python"
text2 = 'Hello Python'

print(text1)
print(text2)
```

Both create strings.

### Checking the type

```python
message = "Learning Python"

print(type(message))
```

Output:

```text
<class 'str'>
```

---

# Strings Can Contain Spaces

Spaces are also part of a string.

```python
message = "Python is fun"

print(message)
```

The spaces between the words are included in the string.

---

# Multiline Strings

Python also allows strings to span multiple lines using triple quotes.

```python
message = """Python is interesting.
I am learning it step by step.
Practice is helping me understand it."""

print(message)
```

Output:

```text
Python is interesting.
I am learning it step by step.
Practice is helping me understand it.
```

Multiline strings are useful when the text itself needs to contain line breaks.

---

# String Length

The `len()` function tells me how many characters are in a string.

```python
word = "Python"

print(len(word))
```

Output:

```text
6
```

The length includes spaces when spaces are part of the string.

```python
message = "Hello Python"

print(len(message))
```

---

# String Indexing

Strings are **ordered sequences of characters**.

Each character has a position called an **index**.

Python uses **zero-based indexing**, which means the first character is at index `0`.

For:

```python
word = "Python"
```

the positions are:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
```

I can access individual characters using their index.

```python
word = "Python"

print(word[0])
print(word[1])
print(word[5])
```

Output:

```text
P
y
n
```

---

# Negative Indexing

Python also allows me to access characters from the end of the string using negative indexes.

```text
 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
```

For example:

```python
word = "Python"

print(word[-1])
print(word[-2])
```

Output:

```text
n
o
```

This is useful when I want to access characters from the end without knowing the exact length of the string.

---

# String Slicing

Indexing gives me one character.

**Slicing lets me extract a portion of the string.**

The basic syntax is:

```python
string[start:stop]
```

The `start` position is included, while the `stop` position is not.

```python
word = "Python"

print(word[0:3])
```

Output:

```text
Pyt
```

The indexes are:

```text
P   y   t   h   o   n
0   1   2   3   4   5
```

The slice `[0:3]` therefore includes indexes `0`, `1`, and `2`.

---

# More Slicing Examples

```python
word = "Python"

print(word[:3])
print(word[3:])
print(word[1:5])
```

Output:

```text
Pyt
hon
ytho
```

I can also use a step.

```python
word = "Python"

print(word[::2])
```

Output:

```text
Pto
```

The step tells Python how many positions to move each time.

---

# Reversing a String

A useful slicing technique is:

```python
word = "Python"

print(word[::-1])
```

Output:

```text
nohtyP
```

Here, the negative step moves through the string backwards.

---

# Strings Are Immutable

One important concept I learned is that Python strings are **immutable**.

That means I cannot directly change an individual character inside an existing string.

For example:

```python
word = "Python"

word[0] = "J"
```

This produces an error.

Instead, I need to create a new string.

```python
word = "Python"

word = "J" + word[1:]

print(word)
```

Output:

```text
Jython
```

The original string was not modified. A new string was created and assigned to the variable.

---

# String Concatenation

I can join strings together using the `+` operator.

```python
first_name = "Hanish"
last_name = "Sharma"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Hanish Sharma
```

This is called **string concatenation**.

---

# String Repetition

The `*` operator can repeat a string.

```python
word = "Hi "

print(word * 3)
```

Output:

```text
Hi Hi Hi 
```

This works because Python allows strings to be multiplied by integers.

---

# Checking for Text

The `in` operator can be used to check wheth
