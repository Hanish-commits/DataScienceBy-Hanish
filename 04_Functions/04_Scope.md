# Scope

**Scope** refers to the part of a Python program where a variable can be accessed.

As I started working with functions, I noticed something important:

A variable created inside a function does not automatically behave like a variable created outside the function.

Understanding scope helps me know:

* where a variable exists
* where I can use it
* what happens when two variables have the same name
* how functions interact with variables outside them

---

# Local Scope

A variable created **inside a function** usually has **local scope**.

```python
def greet():
    name = "Hanish"
    print(name)

greet()
```

Output:

```text
Hanish
```

Here, `name` belongs to the function.

I can use it inside `greet()`.

But:

```python
def greet():
    name = "Hanish"

greet()

print(name)
```

produces a `NameError`.

Why?

Because `name` was created inside `greet()` and is not available in that scope outside the function.

---

# Thinking About Local Scope

I can visualize it like this:

```text
Outside the function
       │
       │
       └── def greet():
               │
               └── name = "Hanish"
```

The variable `name` exists inside the function's local scope.

This is one of the first places where I noticed that **a variable's name alone does not tell me whether I can use it everywhere**.

---

# Global Scope

A variable created outside a function has **global scope** within that module.

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

The function can read the global variable.

So:

```text
Global variable
      ↓
Function can read it
```

---

# Local vs Global

Compare these two examples.

### Local variable

```python
def show_name():
    name = "Hanish"
    print(name)
```

`name` belongs to the function.

### Global variable

```python
name = "Hanish"

def show_name():
    print(name)
```

`name` exists outside the function, so the function can read it.

The location where the variable is created affects its scope.

---

# Local and Global Variables With the Same Name

Python allows a local variable and a global variable to have the same name.

```python
name = "Global Hanish"

def show_name():
    name = "Local Hanish"
    print(name)

show_name()
print(name)
```

Output:

```text
Local Hanish
Global Hanish
```

Inside the function, Python uses the local `name`.

Outside the function, Python uses the global `name`.

This showed me that the same variable name does not necessarily refer to the same variable.

---

# The `global` Keyword

Normally, assigning to a variable inside a function creates a local variable.

For example:

```python
count = 10

def update_count():
    count = 20

update_count()

print(count)
```

Output:

```text
10
```

The function created its own local `count`.

It did not change the global `count`.

---

## Changing a Global Variable

Python provides the `global` keyword when I intentionally want a function to modify a global variable.

```python
count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)
```

Output:

```text
20
```

The `global` statement tells Python that the `count` inside the function refers to the global variable.

---

# Why Should I Be Careful With `global`?

Although `global` exists, I should not automatically use it whenever I want to share data.

Heavy use of global variables can make programs harder to understand because many different parts of the program can change the same value.

For now, the important idea is:

> I can modify a global variable explicitly with `global`, but I should use this deliberately.

Later, parameters and return values will usually give me cleaner ways to move information into and out of functions.

---

# Parameters and Scope

Function parameters are local to the function.

```python
def greet(name):
    print(name)

greet("Hanish")
```

Here, `name` is a local variable inside the function.

I cannot normally access it outside:

```python
def greet(name):
    print(name)

greet("Hanish")

print(name)
```

This raises a `NameError`.

The parameter exists only within the function call's scope.

---

# Return vs Scope

This connects directly to the previous topic.

Suppose:

```python
def get_name():
    name = "Hanish"
    return name
```

The local variable `name` stays inside the function.

But I can send its **value** outside using `return`:

```python
result = get_name()

print(result)
```

Output:

```text
Hanish
```

The variable itself did not become global.

The **value was returned** and stored in a different variable called `result`.

This is a very useful distinction.

---

# Functions Have Their Own Local Scope

Consider:

```python
def first():
    value = 10
    print(value)

def second():
    value = 20
    print(value)

first()
second()
```

Output:

```text
10
20
```

The two `value` variables are local to different functions.

They don't interfere with each other simply because they have the same name.

---

# Nested Functions and Enclosing Scope

A function can also be defined inside another function.

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()
```

Output:

```text
Hello
```

The `inner()` function can access `message` from the enclosing `outer()` function.

This introduces another level of scope.

I don't need to become an expert with nested functions yet, but it is useful to know that Python can have more than just local and global scope.

---

# The LEGB Rule

Python looks for a variable name using a common scope-search order called **LEGB**:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

For example, when Python sees:

```python
print(value)
```

it searches for `value` roughly in this order:

```text
1. Local scope
2. Enclosing scope
3. Global scope
4. Built-in scope
```

This explains why a local variable can take priority over a global variable with the same name.

---

# Example of LEGB

```python
value = "global"

def outer():
    value = "enclosing"

    def inner():
        value = "local"
        print(value)

    inner()

outer()
```

Output:

```text
local
```

Python finds `value` in the nearest available scope first.

If the local variable did not exist, Python could look outward.

---

# Built-in Scope

Python already provides many built-in names, such as:

```python
print
len
type
int
str
```

These are available without creating them ourselves.

For example:

```python
numbers = [10, 20, 30]

print(len(numbers))
```

I can use `len()` because it exists in Python's built-in scope.

---

# A Problem With Shadowing Built-ins

I can technically create a variable using the same name as a built-in:

```python
print = "Hello"

print(print)
```

But now `print` no longer refers to Python's built-in `print()` function in this scope.

This causes problems.

The same thing can happen with names such as:

```python
list
str
sum
type
```

So I should avoid using built-in function names as my own variable or function names.

This is a small naming habit that can prevent confusing errors.

---

# Scope and Loops

Variables created inside a `for` or `while` block behave differently from variables created inside a function.

For example:

```python
for number in range(3):
    print(number)

print(number)
```

In Python, the loop variable still exists after the loop finishes.

This is different from a function's local scope.

So I should not assume:

> "Anything inside an indented block automatically becomes local."

Python's scope rules depend on the kind of block I am working with.

---

# Practical Example

Suppose I want to calculate a total.

```python
price = 500

def calculate():
    quantity = 3
    total = price * quantity
    return total

result = calculate()

print(result)
```

Here:

* `price` → global variable
* `quantity` → local variable
* `total` → local variable
* `result` → variable outside the function

The function can read `price`, create local values, and return the final result.

---

# Better Data Flow Through Parameters and Return

Instead of relying on a global variable:

```python
price = 500

def calculate(quantity):
    return price * quantity
```

I can make the dependency explicit:

```python
def calculate(price, quantity):
    return price * quantity
```

Then:

```python
result = calculate(500, 3)

print(result)
```

This is often easier to understand because the function clearly shows what information it needs.

This connects directly to the previous topics:

**Parameters → send data in**

**Return → send data out**

That makes functions much easier to reuse.

---

# What I Noticed

Scope initially felt like another technical rule to memorize.

But the main idea is simpler:

> **Where a variable is created affects where Python can find it.**

The most important distinction for me is:

**Inside a function → local scope**

**Outside functions → global scope**

And when functions need data, parameters and return values are usually clearer ways to communicate than relying heavily on globals.

---

# What Connected With Previous Topics?

### Functions

Functions create their own local scope.

### Parameters

Parameters are local to the function.

### `return`

A function can send a value outside without exposing its local variable.

### Variables

The same variable name can represent different variables in different scopes.

### Control Flow

Conditions and loops can exist inside functions while using local variables.

This shows how functions are becoming a layer that organizes the Python concepts I already know.

---

# Practice

## Practice 1 — Local Variable

Create a function with a local variable.

Try accessing the variable both inside and outside the function.

Observe what happens.

---

## Practice 2 — Global Variable

Create a global variable and read it from inside a function.

---

## Practice 3 — Same Name

Create:

```python
name = "Global"

def test():
    name = "Local"
    print(name)
```

Call the function and then print `name` outside it.

Predict the output first.

---

## Practice 4 — `global`

Create a global counter.

Write a function that changes it using the `global` keyword.

Observe the difference.

---

## Practice 5 — Parameter vs Global

Write two versions of a calculation:

**Version A:** uses a global variable.

**Version B:** receives the value as a parameter.

Think about which one is easier to reuse and why.

---

## Practice 6 — Return + Scope

Create a function with a local variable and return that value.

Store the returned value outside the function.

Explain the difference between the local variable and the outside variable.

---

## Practice 7 — LEGB

Create a simple nested-function example with:

* a global variable
* an enclosing variable
* a local variable

Observe which value Python uses.

---

## Practice 8 — Naming

Try creating a variable called:

```python
list
```

Then see what happens when you try to use:

```python
list(...)
```

Restore the normal built-in behavior afterward.

---

## My Learning Note

> Scope helped me understand that variables don't automatically exist everywhere in my program. Variables inside functions are local to those functions, while parameters and return values provide a cleaner way to move information between different parts of a program.

---