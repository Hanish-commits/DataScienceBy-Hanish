# Function Basics

Until now, I have been writing code that runs directly when the program reaches it.

Now I am learning how to create a **function** — a reusable block of code that performs a particular task.

The basic idea is:

> **Write the code once → call the function whenever I need it.**

---

# Why Do We Need Functions?

Suppose I need to print the same message several times.

Without a function:

```python
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
```

I am repeating the same code.

Instead, I can put that code inside a function:

```python
def welcome():
    print("Welcome to Python")
```

Then call the function whenever I need it:

```python
welcome()
welcome()
welcome()
```

This helps make code more **reusable and organized**.

---

# Defining a Function

I define a function using the `def` keyword.

```python
def welcome():
    print("Welcome to Python")
```

This creates the function, but it does **not** run it yet.

The function only runs when I call it.

---

# Calling a Function

I call a function by writing its name followed by parentheses:

```python
welcome()
```

Example:

```python
def welcome():
    print("Welcome to Python")

welcome()
```

Output:

```text
Welcome to Python
```

This distinction is important:

```text
def welcome()
        ↓
create the function

welcome()
        ↓
run the function
```

---

# A Function Can Be Called Multiple Times

Once a function exists, I can reuse it.

```python
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()
```

Output:

```text
Welcome to Python
Welcome to Python
Welcome to Python
```

I wrote the instructions once, but I used them three times.

That is one of the main reasons functions are useful.

---

# Function Syntax

The general structure is:

```python
def function_name():
    # code inside the function
```

There are a few important parts:

### `def`

Tells Python that I am defining a function.

### `function_name`

The name I choose for the function.

### `()`

Contains the function's parameters when I eventually use them.

### `:`

Marks the beginning of the function block.

### Indented code

The indented code belongs to the function.

---

# Indentation in Functions

Just like `if` statements and loops, indentation is important.

Correct:

```python
def greet():
    print("Hello")
```

Incorrect:

```python
def greet():
print("Hello")
```

The second version produces an indentation error.

The indentation tells Python which statements belong to the function.

---

# Creating Simple Functions

I can create a function for a specific task.

```python
def say_hello():
    print("Hello!")

def show_course():
    print("I am learning Data Science")

say_hello()
show_course()
```

Output:

```text
Hello!
I am learning Data Science
```

Each function has a clear responsibility.

---

# Functions Help Organize Code

Imagine a program with several tasks:

```python
def show_name():
    print("Hanish")

def show_course():
    print("Data Science")

def show_goal():
    print("Become a Data Scientist")
```

I can decide when each task should happen:

```python
show_name()
show_course()
show_goal()
```

This makes the program easier to organize than placing everything into one long sequence of statements.

---

# Function Names

Function names should describe what the function does.

### Good

```python
def calculate_total():
    ...

def show_profile():
    ...

def print_message():
    ...
```

### Less useful

```python
def abc():
    ...

def x():
    ...
```

Meaningful names make code easier to understand.

Python convention generally uses **snake_case** for function names.

For example:

```python
calculate_total()
show_student_details()
find_maximum()
```

---

# A Function With More Than One Statement

A function can contain multiple lines of code.

```python
def show_profile():
    name = "Hanish"
    age = 30
    course = "Data Science"

    print(name)
    print(age)
    print(course)

show_profile()
```

Output:

```text
Hanish
30
Data Science
```

The whole indented block belongs to the function.

---

# Local Variables Inside a Function

A variable created inside a function is generally available within that function.

```python
def show_name():
    name = "Hanish"
    print(name)

show_name()
```

The variable `name` exists inside the function's scope.

I will study **scope** properly in a later function topic.

For now, I mainly want to understand that functions can have their own variables.

---

# Using Existing Variables

A function can also use a variable that already exists outside it.

```python
name = "Hanish"

def greet():
    print(name)

greet()
```

Output:

```text
Hanish
```

This works, but I need to be careful about how variables are shared between different parts of a program.

That is why **scope** will be an important topic later.

---

# Calling a Function Before Defining It

Python executes code from top to bottom.

So this will cause an error:

```python
greet()

def greet():
    print("Hello")
```

At the point where Python reaches:

```python
greet()
```

the function has not been defined yet.

Usually I should define the function first:

```python
def greet():
    print("Hello")

greet()
```

---

# Functions and Reusability

One of the biggest ideas I am learning is **reusability**.

Without a function:

```python
print("Hello Hanish")
print("Hello Hanish")
print("Hello Hanish")
```

With a function:

```python
def greet():
    print("Hello Hanish")

greet()
greet()
greet()
```

The second approach gives me one place to maintain the instructions.

Later, parameters will allow the same function to work with different values.

---

# A Small Practical Example

I can create a function that displays my current learning status.

```python
def learning_status():
    print("Learning Python")
    print("Building programming foundations")
    print("Working toward Data Science")

learning_status()
```

Output:

```text
Learning Python
Building programming foundations
Working toward Data Science
```

This is still simple, but it shows how a function can package several related instructions together.

---

# What I Noticed

Functions feel different from variables, conditions, and loops.

With a variable, I **store data**.

With an `if` statement, I **make a decision**.

With a loop, I **repeat something**.

With a function, I can **package instructions into a reusable unit**.

This is an important shift in how I think about writing programs.

---

# What Connected With Previous Topics?

Functions can contain concepts I already know.

For example:

### Variables

```python
def show_age():
    age = 30
    print(age)
```

### `if`

```python
def check_age():
    age = 20

    if age >= 18:
        print("Adult")
```

### Loops

```python
def print_numbers():
    for number in range(1, 6):
        print(number)
```

So a function isn't replacing the concepts I already learned.

It gives me a way to **organize those concepts into reusable blocks of code**.

---

# Practice

## Practice 1 — Simple Function

Create a function called `greet()` that prints:

```text
Hello Python
```

Call it three times.

---

## Practice 2 — Personal Information

Create a function that prints:

* your name
* your current learning goal
* the programming language you are learning

---

## Practice 3 — Function With Existing Concepts

Create a function that prints the numbers from `1` to `5` using a `for` loop.

---

## Practice 4 — Function With a Condition

Create a function that stores an age and prints whether the person is an adult or not.

---

## Practice 5 — Reusability

Create two functions:

```text
show_python()
show_data_science()
```

Each should display a relevant message.

Call them in different orders and observe how the program behaves.

---

## Practice 6 — Think Before Running

What will this code do?

```python
def test():
    print("A")
    print("B")

print("Start")
test()
print("End")
```

Predict the output first, then run it.

---

## My Learning Note

> Functions introduced me to the idea of packaging instructions into a reusable block. I am still getting used to thinking about when a function is defined versus when it actually runs, so I want to practice that distinction before moving into parameters and return values.

---
