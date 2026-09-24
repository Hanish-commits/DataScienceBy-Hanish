# Operators

Operators are symbols or keywords that Python uses to perform operations on values.

For example:

```python
a = 10
b = 5

print(a + b)
```

Here, `+` is an operator that tells Python to add the two values.

Operators become important because they allow me to **calculate, compare, assign, and work with data**.

---

## Arithmetic Operators

Arithmetic operators are used for mathematical calculations.

| Operator | Meaning        |   Example | Result |
| -------- | -------------- | --------: | -----: |
| `+`      | Addition       |  `10 + 5` |   `15` |
| `-`      | Subtraction    |  `10 - 5` |    `5` |
| `*`      | Multiplication |  `10 * 5` |   `50` |
| `/`      | Division       |  `10 / 5` |  `2.0` |
| `//`     | Floor Division | `10 // 3` |    `3` |
| `%`      | Modulus        |  `10 % 3` |    `1` |
| `**`     | Exponentiation |  `2 ** 3` |    `8` |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### Output

```text
13
7
30
3.3333333333333335
3
1
1000
```

### What I noticed

`/` and `//` are different.

```python
10 / 3
```

gives the regular division result, while:

```python
10 // 3
```

gives the floor-division result.

The `%` operator gives the **remainder**, which will become useful later when working with conditions and loops.

---

## Assignment Operators

Assignment operators are used to assign or update values.

The basic assignment operator is:

```python
=
```

Example:

```python
score = 100
```

Python also provides compound assignment operators.

```python
score = 100

score += 10
print(score)

score -= 20
print(score)

score *= 2
print(score)
```

### Output

```text
110
90
180
```

For example:

```python
score += 10
```

is another way of writing:

```python
score = score + 10
```

---

## Comparison Operators

Comparison operators are used to compare two values.

The result of a comparison is a Boolean value:

`True` or `False`.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
age = 25

print(age == 25)
print(age != 30)
print(age > 18)
print(age < 18)
print(age >= 25)
print(age <= 20)
```

### Output

```text
True
True
True
False
True
False
```

This is important because comparison operators allow programs to **make decisions based on data**.

I will use them much more when I reach `if` statements and control flow.

---

## Logical Operators

Logical operators are used to combine or modify conditions.

The three main logical operators are:

* `and`
* `or`
* `not`

### `and`

Both conditions must be `True`.

```python
age = 25

print(age > 18 and age < 30)
```

### Output

```text
True
```

### `or`

At least one condition must be `True`.

```python
age = 25

print(age < 18 or age > 20)
```

### Output

```text
True
```

### `not`

`not` reverses a Boolean result.

```python
is_learning = True

print(not is_learning)
```

### Output

```text
False
```

I will understand these operators more naturally when I start working with conditions.

---

## Operator Precedence

Python follows rules that determine which operation is performed first.

For example:

```python
result = 10 + 5 * 2
print(result)
```

### Output

```text
20
```

Multiplication happens before addition.

I can use parentheses when I want to make the order explicit:

```python
result = (10 + 5) * 2
print(result)
```

### Output

```text
30
```

This is a useful habit because parentheses can make my intention clearer.

---

## A Small Practical Example

Operators become more useful when several operations are combined.

```python
price = 500
quantity = 3

total = price * quantity
discount = 100

final_price = total - discount

print(final_price)
```

### Output

```text
1400
```

Here I used:

* `*` to calculate the total
* `-` to subtract the discount
* `=` to store the results

This is a simple example of how operators can work together in a program.

---

## What I Learned

Operators allow me to:

* perform calculations
* update values
* compare values
* work with Boolean conditions
* combine conditions
* control the order of calculations

---

## What I Noticed

Until now, I had mainly been storing and displaying values.

Operators showed me how I can actually **do something with those values**.

I also noticed that some operators, such as comparison and logical operators, produce Boolean results. This connects directly to the control-flow concepts I will learn later.

---

## Practice

### Practice 1 — Calculator

Create two numbers and calculate:

* addition
* subtraction
* multiplication
* division
* modulus

### Practice 2 — Comparison

Create a variable called `age` and check whether:

* it is greater than 18
* it is equal to 18
* it is less than 18

### Practice 3 — Updating a Value

Create:

```python
score = 50
```

Then increase it by `25`, decrease it by `10`, and multiply it by `2` using assignment operators.

Try these yourself before looking for a solution.

---

## My Learning Note

> Operators helped me move from simply storing and displaying values to actually working with them. I am also starting to see how comparisons and Boolean results will eventually help Python make decisions.

---
