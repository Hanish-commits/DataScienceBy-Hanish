# Variables

A variable is one of the first programming concepts I need to understand because it allows me to **store information and use it later in my program**.

Instead of writing the same value repeatedly, I can give it a name and refer to that name.

---

## Creating a Variable

In Python, I can create a variable by assigning a value to a name using `=`.

```python
name = "Hanish"
age = 30
```

Here:

* `name` stores `"Hanish"`
* `age` stores `30`

I can then use those variables in my program.

```python
name = "Hanish"
age = 30

print(name)
print(age)
```

### Output

```text
Hanish
30
```

---

## Assignment Operator `=`

The `=` sign is used for **assignment**.

It means that the value on the right is assigned to the variable on the left.

```python
age = 30
```

This does **not** mean that `age` and `30` are mathematically equal.

It means Python stores the value `30` under the name `age`.

---

## Variables Can Store Different Types of Data

Python variables can hold different kinds of values.

```python
name = "Hanish"
age = 30
height = 5.9
is_learning = True
```

These values represent different data types:

* `"Hanish"` → string
* `30` → integer
* `5.9` → float
* `True` → boolean

I will learn about Python's different data types in more detail in the next topic.

---

## Changing a Variable

A variable's value can be changed.

```python
age = 30
print(age)

age = 31
print(age)
```

### Output

```text
30
31
```

The second assignment changes the value stored in `age`.

---

## Using Variables in Calculations

Variables become more useful when I use them in expressions.

```python
price = 100
quantity = 3

total = price * quantity

print(total)
```

### Output

```text
300
```

Instead of directly writing `100 * 3`, I used variables to make the calculation easier to understand and modify.

---

## Naming Variables

Variable names should be meaningful so that the code is easier to understand.

### Better

```python
student_name = "Hanish"
total_price = 500
```

### Less meaningful

```python
x = "Hanish"
a = 500
```

Python also follows rules for variable names.

For example:

```python
student_name = "Hanish"
age2 = 30
```

are valid names, while:

```python
2age = 30
```

is not valid because a variable name cannot start with a number.

---

## What I Noticed

Variables made Python feel more useful than simply printing text.

With `print()`, I was displaying information.

With variables, I can **store information, reuse it, change it, and use it in calculations**.

This feels like an important step from writing individual statements toward actually building programs.

---

## Practice

### Practice 1

Create variables for:

* your name
* your age
* your city

Then print all three.


### Practice 2

Create a variable called `score`, give it a value, print it, change its value, and print it again.

Try these yourself before looking for a solution.

---

## My Learning Note

> Variables helped me understand that programming is not just about giving instructions. I can store information, give it a meaningful name, and use that information later in my program.

---
