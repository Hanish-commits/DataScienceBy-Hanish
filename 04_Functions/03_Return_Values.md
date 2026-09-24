# Return Values

In the previous topics, I learned how to create functions and pass values into them using parameters and arguments.

Now I am learning one of the most important parts of functions:

> A function can **return a value** back to the place where it was called.

This is different from simply printing something.

---

# `print()` vs `return`

This is the first distinction I really want to understand.

Consider:

```python
def add(a, b):
    print(a + b)

result = add(10, 5)

print(result)
```

The output is:

```text
15
None
```

The function displayed `15`, but it did not send `15` back to `result`.

Now compare that with:

```python
def add(a, b):
    return a + b

result = add(10, 5)

print(result)
```

Output:

```text
15
```

This time, the function **returned** `15`, so I could store it in `result`.

---

# The Key Difference

I can think about it this way:

```text
print()
   ↓
Show something to me

return
   ↓
Send something back to the caller
```

So:

```python
print(10 + 5)
```

displays the result.

But:

```python
return 10 + 5
```

makes the result available to the code that called the function.

---

# A Simple Return Statement

```python
def add(a, b):
    return a + b
```

Calling the function:

```python
result = add(10, 5)

print(result)
```

Output:

```text
15
```

The function calculated the value and returned it.

---

# Returning a Value Does Not Automatically Print It

This is important.

```python
def add(a, b):
    return a + b

add(10, 5)
```

There is no output.

Why?

Because `return` sends the value back, but I didn't tell Python to display it.

I need:

```python
print(add(10, 5))
```

Output:

```text
15
```

This helped me understand that **returning and printing are separate actions**.

---

# Storing a Returned Value

A returned value can be stored in a variable.

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

Output:

```text
25
```

Now `result` contains the value returned by the function.

That means I can use it again:

```python
result = square(5)

print(result)
print(result + 10)
```

Output:

```text
25
35
```

This is one of the major reasons `return` is so useful.

---

# Using a Returned Value in Another Calculation

A returned value does not have to be stored first.

I can use it directly.

```python
def add(a, b):
    return a + b

result = add(10, 5) * 2

print(result)
```

Output:

```text
30
```

The function returns `15`, and that value is then multiplied by `2`.

So the flow is:

```text
add(10, 5)
     ↓
   15
     ↓
15 * 2
     ↓
   30
```

---

# Returning From an `if` Statement

A function can return different values depending on a condition.

```python
def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

Now:

```python
result = check_even(10)

print(result)
```

Output:

```text
Even
```

And:

```python
print(check_even(7))
```

Output:

```text
Odd
```

The function decides what value to return.

---

# `return` Ends the Function

Once Python reaches a `return` statement, the function stops running.

```python
def test():
    print("Start")
    return
    print("End")

test()
```

Output:

```text
Start
```

The `"End"` line is never executed.

This is an important behavior to understand:

```text
Code before return → runs
return → function ends
Code after return → does not run
```

---

# Returning Without a Value

I can also write:

```python
return
```

without specifying a value.

For example:

```python
def stop():
    print("Before return")
    return
    print("After return")

stop()
```

The function ends when it reaches `return`.

In this case, the function returns `None`.

---

# What Is `None`?

`None` represents the absence of a value.

For example:

```python
def greet():
    print("Hello")

result = greet()

print(result)
```

Output:

```text
Hello
None
```

Why is `result` `None`?

Because the function did not return a value.

This is something I need to become comfortable with because not every function has to return something.

---

# Function Without `return`

```python
def greet():
    print("Hello Python")
```

This function performs an action but does not return a useful value.

---

# Function With `return`

```python
def get_greeting():
    return "Hello Python"
```

Now I can use the returned value elsewhere:

```python
message = get_greeting()

print(message)
```

Output:

```text
Hello Python
```

The second function is more flexible because the caller decides what to do with the returned string.

---

# Returning Different Data Types

A function can return many types of values.

### String

```python
def get_name():
    return "Hanish"
```

### Integer

```python
def get_age():
    return 30
```

### Float

```python
def get_price():
    return 99.50
```

### Boolean

```python
def is_adult():
    return True
```

The type depends on what the function returns.

---

# Returning a List

A function can return a list.

```python
def get_fruits():
    return ["apple", "banana", "mango"]

fruits = get_fruits()

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

I can then work with the returned list:

```python
fruits = get_fruits()

print(fruits[0])
```

Output:

```text
apple
```

---

# Returning Multiple Values

Python allows a function to return multiple values.

For example:

```python
def get_numbers():
    return 10, 20

result = get_numbers()

print(result)
```

Output:

```text
(10, 20)
```

Python returns them as a tuple.

I can unpack them:

```python
def get_numbers():
    return 10, 20

a, b = get_numbers()

print(a)
print(b)
```

Output:

```text
10
20
```

This connects directly with the **tuple unpacking** I learned earlier.

---

# A Practical Example — Total Price

Instead of printing the total inside the function:

```python
def calculate_total(price, quantity):
    print(price * quantity)
```

I can return it:

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)

print(total)
```

Output:

```text
1500
```

Now the returned value can be reused:

```python
total = calculate_total(500, 3)

discount = 100

final_price = total - discount

print(final_price)
```

Output:

```text
1400
```

This is a much more flexible pattern.

The function focuses on **calculating**.

The calling code decides what to **do with the result**.

---

# Another Practical Example — Grade

```python
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"
```

Now I can use it:

```python
grade = get_grade(82)

print(grade)
```

Output:

```text
B
```

Or:

```python
print(f"Your grade is {get_grade(95)}")
```

Output:

```text
Your grade is A
```

The function returns a value instead of deciding how it should be displayed.

---

# Combining Input, Function and Return

Now I can connect several concepts I have learned.

```python
def square(number):
    return number * number

number = int(input("Enter a number: "))

result = square(number)

print(f"Square: {result}")
```

The flow is:

```text
User Input
    ↓
Type Conversion
    ↓
Function
    ↓
Return Value
    ↓
Variable
    ↓
Output
```

This is starting to look much more like a real program.

---

# Why `return` Makes Functions Reusable

Compare these two:

### Function that prints

```python
def calculate_total(price, quantity):
    print(price * quantity)
```

### Function that returns

```python
def calculate_total(price, quantity):
    return price * quantity
```

The second version gives me more options.

I can:

```python
total = calculate_total(500, 3)
```

Then:

```python
print(total)
```

or:

```python
discounted = total - 100
```

or:

```python
if total > 1000:
    print("Large order")
```

The returned value can participate in other parts of my program.

---

# A Common Beginner Confusion

I may initially think these are equivalent:

```python
def add(a, b):
    print(a + b)
```

and:

```python
def add(a, b):
    return a + b
```

They are not.

### `print()`

Displays the result.

### `return`

Passes the result back to the caller.

For example:

```python
def add(a, b):
    print(a + b)

result = add(5, 3)

print(result)
```

Output:

```text
8
None
```

But:

```python
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
```

Output:

```text
8
```

This is one of the most important function concepts I have learned so far.

---

# Another Important Point

A `return` statement does not have to return the result of a calculation.

It can return any suitable value.

```python
def get_status():
    return "Learning Python"
```

Or:

```python
def get_status():
    return True
```

Or:

```python
def get_status():
    return [1, 2, 3]
```

The function's purpose determines what it should return.

---

# What I Noticed

This topic helped me understand why some functions feel much more useful than others.

A function that only prints something is useful for displaying information.

A function that returns a value can become part of a larger program.

The biggest distinction I want to remember is:

> **`print()` shows a value. `return` gives a value back.**

---

# What Connected With Previous Topics?

### Parameters

The function can receive values:

```python
def add(a, b):
```

### Operators

The function can process those values:

```python
return a + b
```

### Control Flow

The function can make decisions:

```python
if number % 2 == 0:
    return "Even"
```

### Variables

Returned values can be stored:

```python
result = add(10, 5)
```

### Tuples

Multiple returned values are packed into a tuple:

```python
return 10, 20
```

This is a good example of how the Python concepts I learned earlier are now combining inside functions.

---

# Practice

## Practice 1 — Return a Sum

Create:

```python
add(a, b)
```

that returns the sum instead of printing it.

Store the returned result in a variable and print it.

---

## Practice 2 — Square

Create:

```python
square(number)
```

that returns the square of a number.

Use the returned value in another calculation.

---

## Practice 3 — Even or Odd

Create:

```python
check_even(number)
```

that returns:

```text
"Even"
```

or:

```text
"Odd"
```

Then print the returned value.

---

## Practice 4 — Total Price

Create:

```python
calculate_total(price, quantity)
```

Return the total.

Then apply a discount outside the function.

---

## Practice 5 — Multiple Values

Create a function that returns three values.

Unpack them into three variables.

---

## Practice 6 — `print()` vs `return`

Create two functions:

```text
show_result()
get_result()
```

One should use `print()` and the other should use `return`.

Call both and observe the difference.

---

## Practice 7 — Predict Before Running

What will this produce?

```python
def test():
    print("A")
    return "B"
    print("C")

result = test()

print(result)
```

Predict the output first.

Then run the code and compare.

---

## Practice 8 — Follow the Value

Trace this:

```python
def double(number):
    return number * 2

result = double(10)
final = result + 5

print(final)
```

Try to explain where the value changes at each stage.

---

## My Learning Note

> The difference between `print()` and `return` finally became clearer to me here. `print()` is about displaying something, while `return` allows a function to give a value back so the rest of my program can use it. This makes functions much more reusable.

---
