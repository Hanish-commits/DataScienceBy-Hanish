# Type Conversion

In the previous topic, I learned that `input()` returns a string.

That created a problem when I wanted to perform calculations with user input.

For example:

```python
age = input("Enter your age: ")
```

Even if I enter `30`, Python treats the value as a `str`.

**Type conversion** allows me to change a value from one data type to another.

---

## Why Type Conversion Matters

Different data types behave differently.

For example:

```python
number = "10"
```

Here, `number` is a string.

I cannot treat it exactly like an integer:

```python
print(number + 5)
```

This produces a `TypeError` because Python cannot directly add a string and an integer.

I can convert the string to an integer first:

```python
number = "10"

number = int(number)

print(number + 5)
```

### Output

```text
15
```

---

# Common Conversion Functions

Some common built-in conversion functions are:

| Function  | Converts To | Example         |
| --------- | ----------- | --------------- |
| `int()`   | Integer     | `int("25")`     |
| `float()` | Float       | `float("25.5")` |
| `str()`   | String      | `str(25)`       |
| `bool()`  | Boolean     | `bool(1)`       |

---

## Converting to `int`

The `int()` function converts a value to an integer when the conversion is valid.

```python
age = "30"

age = int(age)

print(age)
print(type(age))
```

### Output

```text
30
<class 'int'>
```

This is especially useful when working with numeric input.

```python
age = int(input("Enter your age: "))

print(age + 1)
```

---

## Converting to `float`

The `float()` function converts a value into a floating-point number.

```python
price = "99.50"

price = float(price)

print(price)
print(type(price))
```

### Output

```text
99.5
<class 'float'>
```

This is useful when working with values such as:

* prices
* measurements
* percentages
* decimal calculations

---

## Converting to `str`

The `str()` function converts a value into a string.

```python
age = 30

age_text = str(age)

print(age_text)
print(type(age_text))
```

### Output

```text
30
<class 'str'>
```

This becomes useful when I need to combine a number with text in situations where a string is required.

---

## Converting to `bool`

The `bool()` function converts a value into either `True` or `False`.

For example:

```python
print(bool(1))
print(bool(0))
```

### Output

```text
True
False
```

Some values are considered **truthy**, while others are **falsy**.

I will understand this more deeply when I start working with conditions.

For now, I mainly need to know that `bool()` can convert values into Boolean values.

---

# Type Conversion vs Type Casting

I will often see the terms **type conversion** and **type casting** used when talking about changing data from one type to another.

For my current learning, I can think of them as the process of converting a value from one data type to another using functions such as:

```python
int()
float()
str()
bool()
```

---

# Conversion Is Not Always Possible

Python cannot convert every value into every type.

For example:

```python
number = int("hello")
```

This produces an error because `"hello"` cannot be interpreted as an integer.

Another example:

```python
number = int("10.5")
```

This also does not work directly because `"10.5"` is written as a decimal string.

Instead:

```python
number = int(float("10.5"))

print(number)
```

### Output

```text
10
```

Here the conversion happens in two stages:

```text
"10.5"
   ↓
10.5
   ↓
10
```

---

# Type Conversion With Input

This is where type conversion becomes especially useful.

Without conversion:

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)
```

If I enter `10` and `20`, the result is:

```text
1020
```

Why?

Because both values are strings, so Python joins them together.

With conversion:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

Now the result is:

```text
30
```

This was an important example for me because the code looks almost identical, but the **data type changes the behavior**.

---

# What I Noticed

This topic connected several things I had already learned:

**Input → String → Type Conversion → Correct Operation**

For example:

```python
age = int(input("Enter your age: "))
```

I am now starting to understand that learning Python is not just about remembering syntax.

I also need to understand **what type of data I am working with**.

---

## Practice

### Practice 1

Convert:

```python
number = "100"
```

into an integer and check its type.

### Practice 2

Convert:

```python
price = "49.99"
```

into a float and multiply it by `2`.

### Practice 3

Ask the user for two numbers and print their sum.

Make sure to convert the input before adding the numbers.

### Practice 4

Create an integer and convert it into a string.

Use `type()` to verify the result.

Try these yourself before looking for a solution.

---

## My Learning Note

> Type conversion helped me understand why Python sometimes behaves differently even when values look similar. `"10"` and `10` may look almost the same to me, but Python treats them as different types.

---

