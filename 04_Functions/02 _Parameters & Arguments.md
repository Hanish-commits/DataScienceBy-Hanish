# Parameters & Arguments

In the previous topic, I learned how to create and call a basic function.

For example:

```python
def greet():
    print("Hello Hanish")
```

This function works, but it is limited because `"Hanish"` is fixed inside the function.

What if I want to greet different people?

This is where **parameters and arguments** become useful.

---

# What is a Parameter?

A **parameter** is a variable written inside the parentheses when I define a function.

```python
def greet(name):
    print(f"Hello {name}")
```

Here:

```text
name
```

is the **parameter**.

I can then pass a value when calling the function:

```python
greet("Hanish")
```

Output:

```text
Hello Hanish
```

---

# What is an Argument?

The actual value I provide when calling the function is called an **argument**.

```python
greet("Hanish")
```

Here:

* `name` → parameter
* `"Hanish"` → argument

A simple way to remember it:

> **Parameter → placeholder in the function definition**

> **Argument → actual value supplied when calling the function**

---

# Why Do We Need Parameters?

Without parameters:

```python
def greet():
    print("Hello Hanish")

greet()
```

The function only works with Hanish.

With a parameter:

```python
def greet(name):
    print(f"Hello {name}")

greet("Hanish")
greet("Rahul")
greet("Priya")
```

Output:

```text
Hello Hanish
Hello Rahul
Hello Priya
```

I wrote the function once, but I can use it with different values.

That is the main reason parameters are useful.

---

# One Parameter

A function can take one parameter.

```python
def square(number):
    print(number * number)

square(5)
```

Output:

```text
25
```

I can use the same function with other numbers:

```python
square(10)
square(3)
```

---

# Multiple Parameters

A function can take multiple parameters.

```python
def add(a, b):
    print(a + b)

add(10, 5)
```

Output:

```text
15
```

Here:

* `a` → first parameter
* `b` → second parameter
* `10` → first argument
* `5` → second argument

The order matters.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Hanish", 30)
```

Output:

```text
My name is Hanish and I am 30 years old.
```

---

# Positional Arguments

By default, arguments are matched according to their position.

```python
def introduce(name, age):
    print(name)
    print(age)

introduce("Hanish", 30)
```

This means:

```text
name ← "Hanish"
age  ← 30
```

If I reverse the arguments:

```python
introduce(30, "Hanish")
```

Python still passes them positionally:

```text
name ← 30
age  ← "Hanish"
```

The function may then behave incorrectly for what I intended.

This is why argument order matters when using positional arguments.

---

# Keyword Arguments

I can also provide arguments by explicitly naming the parameters.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=30, name="Hanish")
```

Output:

```text
My name is Hanish and I am 30 years old.
```

Here, Python matches the values using the parameter names rather than their position.

This can make function calls clearer.

---

# Mixing Positional and Keyword Arguments

I can combine them, but positional arguments must come before keyword arguments.

Valid:

```python
def introduce(name, age, city):
    print(name, age, city)

introduce("Hanish", age=30, city="Bengaluru")
```

This is invalid:

```python
# introduce(name="Hanish", 30, city="Bengaluru")
```

A positional argument cannot come after a keyword argument.

---

# Default Parameters

I can give a parameter a **default value**.

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

Now I can call the function without providing an argument:

```python
greet()
```

Output:

```text
Hello Guest
```

Or I can provide a value:

```python
greet("Hanish")
```

Output:

```text
Hello Hanish
```

The supplied argument replaces the default value.

---

# Multiple Default Parameters

I can have more than one parameter with a default value.

```python
def introduce(name="Guest", city="Unknown"):
    print(f"{name} lives in {city}")

introduce()
introduce("Hanish")
introduce("Hanish", "Bengaluru")
```

Output:

```text
Guest lives in Unknown
Hanish lives in Unknown
Hanish lives in Bengaluru
```

---

# A Parameter Without a Default

A required parameter normally comes before parameters that have defaults.

For example:

```python
def greet(name, message="Welcome"):
    print(f"{message}, {name}")

greet("Hanish")
```

Output:

```text
Welcome, Hanish
```

Python will not allow a required parameter to appear after a default parameter in the definition.

For example, this is invalid:

```python
# def greet(message="Welcome", name):
#     ...
```

---

# Passing Different Data Types

Parameters are not limited to one specific type unless I deliberately enforce that elsewhere.

For example:

```python
def show_value(value):
    print(value)

show_value(10)
show_value("Python")
show_value(5.9)
show_value(True)
```

The same function receives different types of values.

This connects directly to Python's dynamic typing.

---

# Passing a List

I can also pass a list into a function.

```python
def show_fruits(fruits):
    print(fruits)

my_fruits = ["apple", "banana", "mango"]

show_fruits(my_fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

The parameter can refer to the list passed into the function.

---

# Using Previous Concepts Inside a Function

Now I can combine functions with concepts I have already learned.

For example:

```python
def check_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even(10)
check_even(7)
```

Output:

```text
Even
Odd
```

The function receives a value and then uses:

* parameter
* operator
* `if` / `else`

This is where functions start becoming more useful.

---

# A Function Can Have Many Parameters

For example:

```python
def show_profile(name, age, city, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Course: {course}")

show_profile(
    "Hanish",
    30,
    "Bengaluru",
    "Data Science"
)
```

Output:

```text
Name: Hanish
Age: 30
City: Bengaluru
Course: Data Science
```

This works, but I should remember that functions with too many parameters can become harder to use and understand.

For now, I mainly want to understand how multiple parameters work.

---

# Arguments Must Match the Function

Suppose:

```python
def add(a, b):
    print(a + b)
```

Calling:

```python
add(10)
```

does not provide enough arguments.

Python raises a `TypeError`.

Similarly:

```python
add(10, 20, 30)
```

provides too many arguments and also raises a `TypeError`.

So the function definition and the function call need to be compatible.

---

# Positional vs Keyword Arguments

I can compare them directly:

### Positional

```python
def profile(name, age):
    print(name, age)

profile("Hanish", 30)
```

Python matches based on position.

### Keyword

```python
profile(age=30, name="Hanish")
```

Python matches based on parameter names.

The second form can make the meaning of each value clearer.

---

# A Practical Example

Suppose I want to calculate the total price of an item.

```python
def calculate_total(price, quantity):
    total = price * quantity
    print(f"Total: ₹{total}")

calculate_total(500, 3)
calculate_total(120, 5)
```

Output:

```text
Total: ₹1500
Total: ₹600
```

The calculation is written once, but I can use it with different values.

This is a simple example of the kind of reusable logic I will eventually use in larger programs.

---

# Another Practical Example

I can create a function that checks whether someone is eligible based on age.

```python
def check_age(age):
    if age >= 18:
        print("Eligible")
    else:
        print("Not eligible")

check_age(25)
check_age(15)
```

The function itself doesn't need to know where the age came from.

It simply receives a value and performs its task.

Later, I can pass values obtained from `input()`.

---

# Function Calls With Expressions

Arguments don't have to be simple values.

I can pass an expression:

```python
def square(number):
    print(number * number)

square(5 + 2)
```

Output:

```text
49
```

Python evaluates:

```text
5 + 2
```

first and passes `7` into the function.

---

# What I Noticed

Parameters changed the way I look at functions.

Before:

> "This function does this exact thing."

Now:

> "This function performs this task using whatever values I give it."

That makes functions much more flexible.

---

# What Connected With Previous Topics?

### Variables

Parameters behave like names that receive values inside a function call.

### Operators

The values received by parameters can be used in calculations and comparisons.

### Control Flow

A function can contain `if`, `elif`, `else`, and loops.

### Input

Values from `input()` can be passed into functions.

For example:

```python
def greet(name):
    print(f"Hello {name}")

name = input("Enter your name: ")

greet(name)
```

This is an important step toward combining everything I have learned so far.

---

# Practice

## Practice 1 — One Parameter

Create a function called `greet(name)` that prints a greeting.

Call it with at least three different names.

---

## Practice 2 — Two Parameters

Create:

```python
add(a, b)
```

and use it with different numbers.

---

## Practice 3 — Default Parameter

Create a function:

```text
greet(name="Guest")
```

Call it both with and without an argument.

---

## Practice 4 — Keyword Arguments

Create a function that accepts:

* name
* age
* city

Call it using keyword arguments in a different order.

---

## Practice 5 — Even or Odd

Create:

```text
check_even(number)
```

Use an `if` statement and the `%` operator.

---

## Practice 6 — Practical Calculation

Create:

```text
calculate_total(price, quantity)
```

Calculate and print the total.

---

## Practice 7 — Input + Function

Ask the user for their name and pass the result into a `greet()` function.

---

## Practice 8 — Predict Before Running

What will this produce?

```python
def introduce(name, course="Python"):
    print(f"{name} is learning {course}")

introduce("Hanish")
introduce("Rahul", "SQL")
```

Predict the output first, then run it.

---

## My Learning Note

> Parameters and arguments helped me understand how to make a function reusable. Instead of writing separate functions for different values, I can write one function and provide the values it needs when I call it.

---

## Next Step

The next topic is **Return Values**.

This is an especially important distinction for me because I now need to understand the difference between:

```python
print()
```

and

```python
return
```

A function can display a result, but it can also **send a value back to the place where the function was called**.
