# Lambda Functions

I have already learned how to create functions using `def`.

For example:

```python
def square(number):
    return number ** 2
```

Python also provides a way to create small, anonymous functions using the **`lambda`** keyword.

A lambda function is generally used when I need a **small function for a simple expression**, often for a short-lived purpose.

---

# Basic Syntax

The basic structure is:

```python
lambda arguments: expression
```

For example:

```python
square = lambda number: number ** 2

print(square(5))
```

Output:

```text
25
```

Here:

* `lambda` → creates the anonymous function
* `number` → parameter
* `number ** 2` → expression
* `square` → variable referring to the function

---

# Lambda vs Normal Function

The same operation can be written using `def`:

```python
def square(number):
    return number ** 2
```

Or using `lambda`:

```python
square = lambda number: number ** 2
```

Both can be called like this:

```python
print(square(5))
```

Output:

```text
25
```

For simple operations, the lambda version is compact.

However, I don't want to assume that shorter code is always better.

---

# Why Is It Called "Anonymous"?

Lambda functions are often called **anonymous functions** because they don't need a traditional function name when they are created.

For example:

```python
lambda x: x * 2
```

This creates a function without giving it a name directly.

I can assign it to a variable:

```python
double = lambda x: x * 2

print(double(5))
```

But once I assign a lambda to a variable, it does have a name I can use to call it.

---

# One Parameter

A lambda can take one parameter.

```python
double = lambda number: number * 2

print(double(10))
```

Output:

```text
20
```

Another example:

```python
cube = lambda number: number ** 3

print(cube(3))
```

Output:

```text
27
```

---

# Multiple Parameters

A lambda can also take multiple parameters.

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

Another example:

```python
multiply = lambda a, b: a * b

print(multiply(5, 4))
```

Output:

```text
20
```

---

# Lambda With No Parameters

A lambda can also have no parameters.

```python
greeting = lambda: "Hello Python"

print(greeting())
```

Output:

```text
Hello Python
```

This is possible, although lambda functions are generally more useful when they perform a small operation on supplied values.

---

# Lambda Has One Expression

A lambda is designed for a single expression.

For example:

```python
square = lambda number: number ** 2
```

This is valid.

The expression is automatically returned.

So:

```python
square = lambda number: number ** 2
```

is conceptually similar to:

```python
def square(number):
    return number ** 2
```

I don't write `return` inside the lambda.

---

# Lambda With a Condition

I can use a conditional expression inside a lambda.

```python
check_even = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check_even(10))
print(check_even(7))
```

Output:

```text
Even
Odd
```

This works because the entire conditional expression is still a single expression.

---

# Lambda With Strings

Lambda functions are not limited to numbers.

```python
get_length = lambda text: len(text)

print(get_length("Python"))
```

Output:

```text
6
```

Another example:

```python
to_upper = lambda text: text.upper()

print(to_upper("python"))
```

Output:

```text
PYTHON
```

These are simple examples, but they show that a lambda can use operations I already know.

---

# Lambda With Lists

A lambda can receive a list too.

```python
get_first = lambda items: items[0]

numbers = [10, 20, 30]

print(get_first(numbers))
```

Output:

```text
10
```

---

# A Very Important Use: `sorted()`

One of the most useful places to see lambda functions is with `sorted()`.

Suppose I have:

```python
students = [
    ("Hanish", 85),
    ("Rahul", 72),
    ("Priya", 92)
]
```

I can sort them by score:

```python
students = [
    ("Hanish", 85),
    ("Rahul", 72),
    ("Priya", 92)
]

students_sorted = sorted(students, key=lambda student: student[1])

print(students_sorted)
```

Output:

```text
[('Rahul', 72), ('Hanish', 85), ('Priya', 92)]
```

Here:

```python
lambda student: student[1]
```

tells `sorted()`:

> Use the second value of each tuple as the sorting key.

This is one of the most practical reasons I am learning lambda functions.

---

# Sorting in Reverse

I can combine the lambda with `reverse=True`.

```python
students = [
    ("Hanish", 85),
    ("Rahul", 72),
    ("Priya", 92)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(students_sorted)
```

Output:

```text
[('Priya', 92), ('Hanish', 85), ('Rahul', 72)]
```

---

# Sorting Dictionaries

Suppose I have:

```python
students = {
    "Hanish": 85,
    "Rahul": 72,
    "Priya": 92
}
```

I can sort the items by score:

```python
students_sorted = sorted(
    students.items(),
    key=lambda item: item[1]
)

print(students_sorted)
```

Output:

```text
[('Rahul', 72), ('Hanish', 85), ('Priya', 92)]
```

This connects lambda functions with:

* dictionaries
* tuples
* `items()`
* sorting

All of these are concepts I already learned.

---

# Lambda With `map()`

Lambda functions are also commonly used with `map()`.

For example:

```python
numbers = [1, 2, 3, 4]

result = map(lambda number: number * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

Here:

```python
lambda number: number * 2
```

describes what should happen to each value.

I will study `map()` properly in the next topic, so for now this is just an introduction to where lambda functions are commonly used.

---

# Lambda With `filter()`

Similarly:

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6]
```

Again, `filter()` itself is a separate topic.

The important observation for now is that lambda functions are often passed as arguments to other functions.

---

# Functions as Values

One thing that lambda functions help me understand is that **functions can be treated like values in Python**.

For example:

```python
def square(number):
    return number ** 2

operation = square

print(operation(5))
```

Output:

```text
25
```

The function is stored in the variable `operation`.

A lambda works similarly:

```python
operation = lambda number: number ** 2

print(operation(5))
```

This is an important Python concept because it helps explain why functions can be passed to other functions.

---

# Passing a Function to Another Function

For example:

```python
def apply_operation(number, operation):
    return operation(number)
```

I can pass a normal function:

```python
def square(number):
    return number ** 2

print(apply_operation(5, square))
```

Or a lambda:

```python
print(apply_operation(5, lambda number: number ** 2))
```

Both produce:

```text
25
```

This is one of the ideas behind higher-order functions.

I don't need to go deeply into that concept yet, but I should recognize what is happening.

---

# Lambda Is Not a Replacement for `def`

It might be tempting to think:

> "Lambda is a shorter way to write every function."

That is not the goal.

For example, this is much clearer as a normal function:

```python
def calculate_student_result(marks, attendance, assignment_score):
    # several lines of logic
    ...
```

Trying to force complicated logic into a lambda would make the code harder to understand.

Lambda is best suited to **small, simple expressions**.

---

# When Lambda Makes Sense

A lambda can be useful when:

* the operation is very small
* I need a function temporarily
* another function expects a function as an argument
* I want to specify a sorting/filtering key

For example:

```python
sorted(
    students,
    key=lambda student: student[1]
)
```

This is compact while still being understandable.

---

# When `def` Is Better

A normal function is usually clearer when:

* the logic has multiple steps
* the function is reused frequently
* the operation deserves a meaningful name
* documentation is useful
* debugging the function separately would help

For example:

```python
def calculate_total(price, quantity):
    return price * quantity
```

This is clearer than forcing the same logic into a lambda.

---

# A Common Beginner Mistake

Trying to put multiple statements inside a lambda is not valid.

For example, this is not valid lambda syntax:

```python
# lambda x:
#     y = x * 2
#     return y
```

A lambda is limited to an expression.

When the logic needs multiple statements, I should use `def`.

---

# Another Beginner Mistake

Don't confuse:

```python
lambda x: x * 2
```

with:

```python
lambda x: print(x * 2)
```

The first returns a value.

The second calls `print()` and therefore returns `None` after displaying the value.

That difference becomes important when a function expects a useful returned result.

---

# A Practical Example — Sorting Products

Suppose:

```python
products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Mouse", "price": 1500},
    {"name": "Keyboard", "price": 3000}
]
```

I can sort the products by price:

```python
sorted_products = sorted(
    products,
    key=lambda product: product["price"]
)

print(sorted_products)
```

The lambda tells `sorted()` which value to use as the sorting key.

This is a much more realistic use of lambda than simply writing:

```python
square = lambda x: x ** 2
```

---

# What I Noticed

Lambda functions initially looked like a completely new type of function.

After experimenting, I can see that the underlying idea is still familiar:

**Input → operation → result**

The main difference is the compact syntax.

The part that feels more important than the syntax is understanding that Python can **pass functions around as values**.

---

# What Connected With Previous Topics?

### Functions

Lambda is another way to create a small function.

### Parameters

A lambda can accept parameters.

### Return Values

The expression in a lambda produces the returned result automatically.

### Lists & Dictionaries

Lambda functions can work with their data.

### Tuples

Sorting tuples with `lambda` is a common example.

### `sorted()`

Lambda can tell `sorted()` what value to use as its sorting key.

The next topic, `map()`, `filter()`, `zip()`, and `enumerate()`, will build directly on these ideas.

---

# Practice

## Practice 1 — Double

Create a lambda that doubles a number.

---

## Practice 2 — Square

Create a lambda that returns the square of a number.

---

## Practice 3 — Two Parameters

Create a lambda that multiplies two numbers.

---

## Practice 4 — Even or Odd

Create a lambda that returns `"Even"` or `"Odd"`.

---

## Practice 5 — String Length

Create a lambda that returns the length of a string.

---

## Practice 6 — Sort Tuples

Given:

```python
students = [
    ("Hanish", 85),
    ("Rahul", 72),
    ("Priya", 92)
]
```

sort the students by their marks using `sorted()` and a lambda.

---

## Practice 7 — Sort Dictionaries

Given:

```python
products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Mouse", "price": 1500},
    {"name": "Keyboard", "price": 3000}
]
```

sort them by price using a lambda.

---

## Practice 8 — Think Before Running

What will this produce?

```python
double = lambda x: x * 2

result = double(5)

print(result)
```

Predict first, then run it.

---

## Practice 9 — `print()` vs Returned Value

What is the difference between:

```python
lambda x: x * 2
```

and:

```python
lambda x: print(x * 2)
```

Think about what each one returns.

---

## Practice 10 — Choose `lambda` or `def`

For each situation, decide which is more appropriate:

**A:** Sort a list using a temporary key.

**B:** Calculate a complicated salary calculation involving several steps.

**C:** Quickly double a value inside another operation.

**D:** A reusable function that your program calls many times.

The important part is explaining **why**.

---

## My Learning Note

> Lambda functions introduced me to a shorter way of creating small functions. The syntax is compact, but I don't want to use lambda just to make code shorter. The most useful connection for me was seeing lambda with `sorted()`, and understanding that functions can be passed around like values.

---