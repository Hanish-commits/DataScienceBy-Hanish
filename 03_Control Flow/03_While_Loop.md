# While Loops

A `while` loop repeats a block of code **as long as a condition remains `True`**.

The basic structure is:

```python
while condition:
    # code to repeat
```

For example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

Python keeps checking the condition.

```text
Check condition
      ↓
   True?
   /   \
 Yes    No
  ↓      ↓
Run     Stop
code
  ↓
Check again
```

---

# How a `while` Loop Works

Consider:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

I can trace it step by step:

```text
count = 1
1 <= 3 → True → print 1 → count becomes 2

count = 2
2 <= 3 → True → print 2 → count becomes 3

count = 3
3 <= 3 → True → print 3 → count becomes 4

count = 4
4 <= 3 → False → stop
```

This step-by-step way of tracing the loop is useful because `while` loops can become confusing if I don't track how the variables change.

---

# A `while` Loop Needs a Changing Condition

A common beginner mistake is creating a condition that never becomes `False`.

For example:

```python
count = 1

while count <= 5:
    print(count)
```

Here, `count` never changes.

The condition will continue to be `True`, so the loop keeps running.

This is called an **infinite loop**.

I need to update the relevant variable:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Now the loop eventually stops.

---

# Incrementing a Variable

The `+=` operator I learned earlier is often useful with `while` loops.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

The important part is:

```python
count += 1
```

It changes the value after each iteration.

I can also use:

```python
count -= 1
```

to count backwards.

---

# Counting Backwards

```python
count = 5

while count >= 1:
    print(count)
    count -= 1
```

Output:

```text
5
4
3
2
1
```

The loop stops when `count >= 1` becomes `False`.

---

# `while` With User Input

A `while` loop becomes especially useful when I want to keep asking for input until the user provides something that satisfies a condition.

For example:

```python
number = int(input("Enter a positive number: "))

while number <= 0:
    number = int(input("Please enter a positive number: "))

print(f"You entered {number}")
```

The program keeps asking until the condition becomes `False`.

The flow is:

```text
Get input
   ↓
Is number <= 0?
   ↓
Yes → Ask again
   ↓
No → Continue
```

This is a different kind of repetition from the `for` loop.

---

# `while` vs `for`

This is one of the most important comparisons in this topic.

### `for`

I generally use a `for` loop when I know I want to go through the items of something.

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

### `while`

I use a `while` loop when the repetition depends on a condition.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

A simple way for me to remember it:

**`for` → "for each item"**

**`while` → "while this is true"**

---

# `while` With `if`

I can use `if` inside a `while` loop.

```python
number = 1

while number <= 10:
    if number % 2 == 0:
        print(number)

    number += 1
```

Output:

```text
2
4
6
8
10
```

Here:

* `while` controls the repetition
* `if` controls which values are printed
* `%` checks whether a number is even

This combines several concepts I have already learned.

---

# Accumulating a Result

Just like with `for` loops, I can build a result step by step.

For example, calculating the total from `1` to `5`:

```python
number = 1
total = 0

while number <= 5:
    total = total + number
    number += 1

print(total)
```

Output:

```text
15
```

I can trace the `total`:

```text
Start → 0

+1 → 1
+2 → 3
+3 → 6
+4 → 10
+5 → 15
```

This is the same accumulation idea I saw with `for` loops, but the repetition is controlled by a condition.

---

# `while` With a Boolean Variable

A Boolean variable can also control a loop.

```python
running = True

while running:
    print("Program is running")

    running = False
```

Output:

```text
Program is running
```

After the first iteration, `running` becomes `False`, so the loop stops.

This pattern becomes more useful in larger programs.

---

# `while True`

Python allows:

```python
while True:
    print("This keeps running")
```

This creates an intentionally infinite loop.

Normally, I would need some way to exit it, which is where `break` becomes useful.

For now, I mainly need to understand that:

```python
while True:
```

means the condition is always `True`.

---

# Common Beginner Mistakes

## Mistake 1 — Forgetting to Update the Variable

Incorrect:

```python
count = 1

while count <= 5:
    print(count)
```

There is nothing changing `count`.

This creates an infinite loop.

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Mistake 2 — Updating in the Wrong Direction

For example:

```python
count = 1

while count <= 5:
    print(count)
    count -= 1
```

The value moves away from the stopping condition instead of toward it.

It becomes:

```text
1 → 0 → -1 → -2 → ...
```

The condition `count <= 5` remains `True`.

This is another example of why tracing the variable matters.

---

## Mistake 3 — Wrong Starting Value

Consider:

```python
count = 10

while count < 5:
    print(count)
```

The condition is already `False`, so the loop never runs.

A `while` loop can therefore execute **zero times** if its initial condition is `False`.

---

# A Practical Example — Password Attempts

A `while` loop can repeat until the correct input is provided.

```python
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")
```

The loop continues while the entered password is incorrect.

This is a practical example of **condition-controlled repetition**.

> For real applications, hard-coding passwords like this is not secure. Here it is only being used to understand the loop.

---

# A Practical Example — Menu

A loop can keep a program running until the user chooses to exit.

```python
choice = ""

while choice != "q":
    print("Enter q to quit")
    choice = input("Your choice: ")

print("Program ended")
```

This pattern shows how a loop can keep a program active until a condition changes.

I will explore more sophisticated versions of this idea later.

---

# `while` Loop With `else`

Python also allows an `else` block after a `while` loop.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed")
```

Output:

```text
1
2
3
Loop completed
```

The `else` runs when the loop finishes normally.

Later, `break` will add another important behavior to this structure.

---

# A Small Comparison With `for`

Suppose I want to print numbers from `1` to `5`.

Using `for`:

```python
for number in range(1, 6):
    print(number)
```

Using `while`:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Both produce:

```text
1
2
3
4
5
```

But the way I control the repetition is different.

With `for`, `range()` controls the sequence.

With `while`, **I am responsible for managing the condition and updating the variable**.

---

# What I Noticed

`while` loops initially feel more difficult than `for` loops because I have more responsibility.

With a `for` loop, Python handles moving through the sequence.

With a `while` loop, I need to think about:

**Where does the loop start?**

**What condition should keep it running?**

**What changes after each iteration?**

**What eventually makes the condition `False`?**

That last part is especially important for avoiding infinite loops.

---

# What Connected With Previous Topics?

### Variables

A variable often controls the loop.

### Operators

Comparison operators determine whether the loop continues.

### `if`

Conditions can be placed inside the loop.

### User Input

`input()` can provide changing information during repetition.

### Arithmetic

Operators such as `+=` and `-=` can update loop variables.

### Lists & Other Data

A `while` loop can also be used to process collections, although `for` is often more natural when iterating directly through a collection.

---

# Practice

## Practice 1 — Counting

Use a `while` loop to print numbers from `1` to `10`.

---

## Practice 2 — Countdown

Print:

```text
5
4
3
2
1
```

using a `while` loop.

---

## Practice 3 — Even Numbers

Use a `while` loop to print the even numbers from `1` to `20`.

---

## Practice 4 — Sum

Use a `while` loop to calculate the sum of numbers from `1` to `10`.

Do not use `sum()`.

---

## Practice 5 — User Input

Keep asking the user to enter a positive number until they enter one.

---

## Practice 6 — Password

Keep asking the user for a password until the expected password is entered.

Use a variable and a condition to control the loop.

---

## Practice 7 — Trace Before Running

Predict the output:

```python
number = 1

while number <= 4:
    print(number)
    number += 1
```

Then run it and compare your prediction.

---

## Practice 8 — Find the Problem

What is wrong with this code?

```python
number = 10

while number <= 20:
    print(number)
    number -= 1
```

Don't just fix it. Explain **why** it does not behave as intended.

---

## My Learning Note

> `while` loops helped me understand that repetition can be controlled by a condition rather than a fixed collection. The part I need to pay the most attention to is how the loop variable changes, because that determines whether the loop eventually stops.

---

