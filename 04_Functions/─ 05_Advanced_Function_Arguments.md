# Advanced Function Arguments

So far, I have learned how to pass normal positional arguments, keyword arguments, and default values to functions.

For example:

```python
def greet(name, message="Welcome"):
    print(f"{message}, {name}")

greet("Hanish")
```

But sometimes I don't know in advance how many arguments a function will receive.

Python provides:

* `*args`
* `**kwargs`

to handle a flexible number of arguments.

---

# Why Do We Need `*args` and `**kwargs`?

Suppose I create:

```python
def add(a, b):
    return a + b
```

This works for two numbers.

But what if I want to add three numbers?

```python
add(10, 20, 30)
```

The function doesn't accept three arguments.

I could keep adding parameters:

```python
def add(a, b, c, d, e):
    ...
```

but that isn't flexible.

This is where `*args` can help.

---

# `*args`

`*args` allows a function to receive a variable number of **positional arguments**.

```python
def add(*args):
    print(args)
```

Now I can call:

```python
add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40, 50)
```

The arguments are collected into a **tuple**.

For example:

```python
add(10, 20, 30)
```

means that inside the function:

```text
args → (10, 20, 30)
```

This connects directly to the tuple concept I learned earlier.

---

# Using `*args`

By itself, `*args` collects the values.

```python
def show_numbers(*args):
    print(args)

show_numbers(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

The name `args` is a convention.

Python doesn't require that exact name.

This also works:

```python
def show_numbers(*numbers):
    print(numbers)
```

However, `*args` is the conventional and most recognizable name.

---

# Working With the Values Inside `args`

Since `args` is a tuple, I can work with it like a tuple.

```python
def show_numbers(*args):
    print(len(args))
    print(args[0])
    print(args[-1])

show_numbers(10, 20, 30, 40)
```

Output:

```text
4
10
40
```

I can also loop through the values:

```python
def show_numbers(*args):
    for number in args:
        print(number)

show_numbers(10, 20, 30)
```

Output:

```text
10
20
30
```

This is where the concepts I learned earlier begin working together:

**Function → `*args` → Tuple → Loop**

---

# A Practical `*args` Example

I can create a function that calculates the total of any number of values.

```python
def calculate_total(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

Now:

```python
print(calculate_total(10, 20))
print(calculate_total(10, 20, 30))
print(calculate_total(10, 20, 30, 40, 50))
```

Output:

```text
30
60
150
```

The function doesn't need to know beforehand how many numbers it will receive.

---

# `*args` Does Not Mean "Any Type"

`*args` means:

> Collect multiple positional arguments.

The arguments can still be different types.

For example:

```python
def show_values(*args):
    print(args)

show_values("Python", 10, True, 5.9)
```

Output:

```text
('Python', 10, True, 5.9)
```

Python allows this, although whether mixed types make sense depends on what the function is supposed to do.

---

# `**kwargs`

`**kwargs` allows a function to receive a variable number of **keyword arguments**.

Example:

```python
def show_profile(**kwargs):
    print(kwargs)
```

Now:

```python
show_profile(
    name="Hanish",
    age=30,
    city="Bengaluru"
)
```

The keyword arguments are collected into a **dictionary**.

Conceptually:

```text
kwargs →
{
    "name": "Hanish",
    "age": 30,
    "city": "Bengaluru"
}
```

This connects directly to the dictionary concept I learned earlier.

---

# Working With `**kwargs`

Because `kwargs` is a dictionary, I can use dictionary operations.

```python
def show_profile(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])
    print(kwargs["city"])

show_profile(
    name="Hanish",
    age=30,
    city="Bengaluru"
)
```

Output:

```text
Hanish
30
Bengaluru
```

I can also use `.items()`:

```python
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_profile(
    name="Hanish",
    age=30,
    city="Bengaluru"
)
```

Output:

```text
name Hanish
age 30
city Bengaluru
```

Again, several earlier concepts are working together.

---

# `*args` vs `**kwargs`

The simplest distinction is:

```text
*args
↓
variable number of positional arguments
↓
tuple

**kwargs
↓
variable number of keyword arguments
↓
dictionary
```

For example:

```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)
```

Calling:

```python
example(10, 20, name="Hanish", age=30)
```

produces something like:

```text
(10, 20)
{'name': 'Hanish', 'age': 30}
```

---

# Combining Normal Parameters With `*args`

I can have regular parameters before `*args`.

```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}")

greet("Hello", "Hanish", "Rahul", "Priya")
```

Output:

```text
Hello, Hanish
Hello, Rahul
Hello, Priya
```

Here:

```text
greeting → "Hello"
names → ("Hanish", "Rahul", "Priya")
```

---

# Combining Normal Parameters With `**kwargs`

I can also combine a normal parameter with `**kwargs`.

```python
def show_course(course, **details):
    print(f"Course: {course}")
    print(details)

show_course(
    "Data Science",
    duration="12 months",
    mode="Online"
)
```

The function receives:

```text
course → "Data Science"

details →
{
    "duration": "12 months",
    "mode": "Online"
}
```

---

# Using Both `*args` and `**kwargs`

A function can accept both.

```python
def profile(name, *skills, **details):
    print(name)
    print(skills)
    print(details)

profile(
    "Hanish",
    "Python",
    "SQL",
    city="Bengaluru",
    goal="Data Science"
)
```

Conceptually:

```text
name →
"Hanish"

skills →
("Python", "SQL")

details →
{
    "city": "Bengaluru",
    "goal": "Data Science"
}
```

This is powerful, but I don't need to use this style everywhere.

It should be used when the flexibility is actually useful.

---

# Keyword-Only Arguments

Python can also force certain arguments to be passed using their names.

For example:

```python
def create_profile(name, *, age, city):
    print(name, age, city)
```

Now this works:

```python
create_profile(
    "Hanish",
    age=30,
    city="Bengaluru"
)
```

But this does not:

```python
# create_profile("Hanish", 30, "Bengaluru")
```

The `*` in the function definition separates the normal positional argument from the **keyword-only arguments**.

This can make function calls clearer when the meaning of the values matters.

---

# Positional-Only Arguments

Python also supports positional-only parameters using `/`.

For example:

```python
def calculate(a, b, /):
    return a + b
```

These parameters must be supplied positionally:

```python
calculate(10, 20)
```

but not:

```python
# calculate(a=10, b=20)
```

This is a more advanced feature.

For my current level, I mainly need to **recognize what `/` means** rather than use positional-only parameters frequently.

---

# Argument Unpacking

The `*` symbol can also be used when **calling** a function.

Suppose:

```python
numbers = [10, 20, 30]
```

and:

```python
def add(a, b, c):
    return a + b + c
```

I can unpack the list:

```python
result = add(*numbers)

print(result)
```

Output:

```text
60
```

The list:

```text
[10, 20, 30]
```

is unpacked into:

```text
10, 20, 30
```

This is a different use of `*` from defining `*args`, but the same general idea of unpacking is involved.

---

# Dictionary Unpacking With `**`

The same idea works with dictionaries.

```python
details = {
    "name": "Hanish",
    "age": 30
}
```

Suppose:

```python
def show_profile(name, age):
    print(name, age)
```

I can write:

```python
show_profile(**details)
```

Python matches:

```text
name → "Hanish"
age  → 30
```

This is useful when data is already stored in a dictionary.

---

# A Practical Example

Imagine I have product details:

```python
product = {
    "name": "Laptop",
    "price": 75000,
    "quantity": 2
}
```

I can pass the dictionary into a matching function:

```python
def show_product(name, price, quantity):
    print(f"Product: {name}")
    print(f"Price: ₹{price}")
    print(f"Quantity: {quantity}")

show_product(**product)
```

The dictionary keys match the function parameter names.

This is a useful pattern when working with structured data.

---

# Common Beginner Mistakes

## Mistake 1 — Thinking `args` Is a List

It isn't.

```python
def show(*args):
    print(type(args))
```

Output:

```text
<class 'tuple'>
```

`*args` collects positional arguments into a **tuple**.

---

## Mistake 2 — Thinking `kwargs` Is a Tuple

It isn't.

```python
def show(**kwargs):
    print(type(kwargs))
```

Output:

```text
<class 'dict'>
```

`**kwargs` collects keyword arguments into a **dictionary**.

---

## Mistake 3 — Confusing Definition and Calling

These are different:

```python
def show(*args):
    ...
```

and:

```python
show(*numbers)
```

In the first case, `*args` **collects** arguments.

In the second case, `*numbers` **unpacks** an existing collection.

This distinction is important.

---

## Mistake 4 — Using `*args` Everywhere

Just because Python allows flexible arguments doesn't mean every function should use them.

If a function clearly needs:

```python
def calculate_total(price, quantity):
```

there is no reason to replace it with:

```python
def calculate_total(*args):
```

The explicit version can be easier to understand.

I want to use flexible arguments when they actually solve a problem.

---

# What I Noticed

`*args` and `**kwargs` initially look complicated because the same symbols can be used in more than one way.

The simplest mental model for me is:

```text
*args
→ collect positional arguments
→ tuple

**kwargs
→ collect keyword arguments
→ dictionary
```

And when used during a function call:

```text
*collection
→ unpack positional values

**dictionary
→ unpack keyword values
```

That makes the behavior easier to reason about.

---

# What Connected With Previous Topics?

### Tuples

`*args` stores positional arguments as a tuple.

### Dictionaries

`**kwargs` stores keyword arguments as a dictionary.

### Functions

Both are tools for making function interfaces more flexible.

### Loops

I can loop through `args` or `kwargs.items()`.

### Lists

A list can be unpacked using `*`.

### Dictionaries

A dictionary can be unpacked using `**`.

This is a good example of how Python keeps reusing concepts I have already learned.

---

# Practice

## Practice 1 — `*args`

Create a function that accepts any number of numbers and prints them.

---

## Practice 2 — Count Arguments

Create a function using `*args` that tells you how many positional arguments were provided.

---

## Practice 3 — Total

Create a function using `*args` that calculates the total of any number of numbers.

Don't use `sum()` yet. Practice the loop.

---

## Practice 4 — `**kwargs`

Create a function using `**kwargs` that prints the received dictionary.

Call it with:

* name
* age
* city
* course

---

## Practice 5 — `**kwargs` With a Loop

Loop through `kwargs.items()` and print each key and value.

---

## Practice 6 — Combine Them

Create:

```python
def profile(name, *skills, **details):
    ...
```

Call it with a name, several skills, and additional information such as city or course.

---

## Practice 7 — Unpacking

Create:

```python
numbers = [10, 20, 30]
```

and a function that accepts three parameters.

Call the function using:

```python
*
```

to unpack the list.

---

## Practice 8 — Dictionary Unpacking

Create a dictionary whose keys match the parameters of a function.

Call the function using:

```python
**
```

to unpack the dictionary.

---

## Practice 9 — Think Before Running

What will this produce?

```python
def test(*args):
    print(args)
    print(type(args))

test(10, 20, 30)
```

Predict the output before running it.

---

## Practice 10 — Explain the Symbols

In your own words, explain the difference between:

```text
*args
**kwargs
*list_name
**dict_name
```

This is more valuable than memorizing the syntax.

---

## My Learning Note

> `*args` and `**kwargs` helped me understand how Python can make functions flexible. The most important thing for me is remembering that `*args` collects positional arguments into a tuple, while `**kwargs` collects keyword arguments into a dictionary. I also learned that `*` and `**` can be used for unpacking when calling a function.

---

# 04 — Functions: Complete

I have now covered the main function concepts in this stage:

```text
Function Basics
      ↓
Parameters & Arguments
      ↓
Return Values
      ↓
Scope
      ↓
Advanced Arguments
```

The most important function flow I have learned is:

```text
Arguments
    ↓
Parameters
    ↓
Function processes the data
    ↓
Return value
```

I now have the foundation needed to start writing functions that are more reusable and structured.
