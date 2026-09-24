# Break, Continue & Pass

So far, I have learned how to create conditions using `if` statements and repeat code using `for` and `while` loops.

Now I am learning three Python statements that can change the normal flow of a loop:

* `break`
* `continue`
* `pass`

They may look similar at first, but they do very different things.

---

# `break`

`break` **stops the loop completely**.

For example:

```python
for number in range(1, 10):
    if number == 5:
        break

    print(number)
```

Output:

```text
1
2
3
4
```

When `number` becomes `5`, the `break` statement is executed and the entire loop stops.

The flow is:

```text
1 → print
2 → print
3 → print
4 → print
5 → break → stop loop
```

---

# `break` With a `while` Loop

`break` works with `while` loops too.

```python
number = 1

while number <= 10:
    if number == 5:
        break

    print(number)
    number += 1
```

Output:

```text
1
2
3
4
```

Even though the original condition allows the loop to continue until `10`, `break` ends it early.

---

# Practical Example: Stop When Found

Suppose I want to search through a list and stop when I find a particular value.

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Found!")
        break

    print(number)
```

Output:

```text
10
20
Found!
```

Once the required value is found, there is no reason to continue searching.

This is one practical way to think about `break`:

> **"I found what I was looking for, so stop."**

---

# `continue`

`continue` does **not** stop the loop.

Instead, it skips the rest of the current iteration and moves to the next iteration.

For example:

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

When `number` is `3`, Python skips the `print()` statement and moves directly to the next iteration.

The loop itself continues.

---

# Understanding `continue`

I can think about it like this:

```text
1 → print
2 → print
3 → continue → skip
4 → print
5 → print
```

So:

```text
break    → stop the entire loop
continue → skip this iteration
```

This distinction is very important.

---

# `continue` With a `while` Loop

`continue` also works with `while`.

```python
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

Notice that I updated `number` **before** `continue`.

That is important with `while` loops.

---

# A Common `while` Loop Mistake

Consider:

```python
number = 1

while number <= 5:
    if number == 3:
        continue

    print(number)
    number += 1
```

This creates a problem.

When `number` becomes `3`, `continue` runs before `number += 1`.

So `number` stays `3`, and the condition:

```python
number <= 5
```

continues to be `True`.

The loop gets stuck.

A safer structure is:

```python
number = 1

while number <= 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

or to make sure the variable is updated on every path.

This was an important lesson for me:

> With `while` loops, I need to be careful that `continue` does not skip the code responsible for changing the loop condition.

---

# `pass`

`pass` is different from both `break` and `continue`.

`pass` **does nothing**.

It is used when Python expects a statement, but I don't want to perform any action yet.

For example:

```python
if True:
    pass
```

The program does nothing inside the block.

---

# Why Do I Need `pass`?

Python does not allow an empty code block.

For example:

```python
if age >= 18:
```

would be incomplete.

If I haven't decided what the code should do yet, I can temporarily use:

```python
if age >= 18:
    pass
```

This allows the program structure to exist without performing an action.

---

# `pass` in a Loop

I can also use `pass` inside a loop.

```python
for number in range(5):
    if number == 2:
        pass

    print(number)
```

Output:

```text
0
1
2
3
4
```

The loop does not skip `2`.

This is an important difference from `continue`.

```text
pass      → do nothing, then continue normally
continue  → skip the rest of this iteration
break     → stop the entire loop
```

---

# `break` vs `continue` vs `pass`

| Statement  | What it does                |
| ---------- | --------------------------- |
| `break`    | Stops the entire loop       |
| `continue` | Skips the current iteration |
| `pass`     | Does nothing                |

A simple mental model:

```text
break
↓
"Stop."

continue
↓
"Skip this one."

pass
↓
"Do nothing here."
```

---

# Combining `if` and `break`

A common pattern is to use an `if` condition to decide when a loop should stop.

```python
numbers = [5, 10, 15, 20, 25]

for number in numbers:
    if number > 15:
        break

    print(number)
```

Output:

```text
5
10
15
```

The loop stops as soon as a value greater than `15` is encountered.

---

# Combining `if` and `continue`

I can use `continue` to ignore specific values.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

The loop continues, but `3` is skipped.

---

# Combining `if` and `pass`

I can use `pass` when I intentionally don't want anything to happen for a particular case.

```python
numbers = [1, 2, 3]

for number in numbers:
    if number == 2:
        pass

    print(number)
```

Output:

```text
1
2
3
```

Nothing special happens when the value is `2`.

---

# A Practical Example: Search

Suppose I want to check whether a name exists in a list.

```python
names = ["Hanish", "Rahul", "Priya", "Aman"]

for name in names:
    if name == "Priya":
        print("Name found")
        break
```

Once the name is found, the search ends.

---

# A Practical Example: Skip Invalid Values

Suppose I have a list containing some negative numbers and I only want to process positive values.

```python
numbers = [10, -5, 20, -2, 30]

for number in numbers:
    if number < 0:
        continue

    print(number)
```

Output:

```text
10
20
30
```

The negative values are skipped.

---

# A Practical Example: User Input

`break` becomes especially useful when working with `while True`.

```python
while True:
    command = input("Enter 'q' to quit: ")

    if command == "q":
        break

    print(f"You entered: {command}")

print("Program ended")
```

The loop continues until the user enters `q`.

The flow is:

```text
Start loop
   ↓
Get input
   ↓
Is input "q"?
   ├── Yes → break → Stop
   └── No  → process input → repeat
```

This is a pattern I will see frequently in Python programs.

---

# `break` in Nested Loops

A `break` statement stops the **nearest loop containing it**.

For example:

```python
for row in range(3):
    for column in range(3):
        if column == 1:
            break

        print(row, column)
```

Output:

```text
0 0
1 0
2 0
```

The `break` stops the inner loop, not the outer loop.

This is useful to know when working with nested loops.

---

# Loop `else` and `break`

Earlier, I saw that Python allows an `else` block after a loop.

This becomes more interesting with `break`.

```python
for number in range(5):
    if number == 10:
        break
else:
    print("Loop completed without break")
```

Output:

```text
Loop completed without break
```

Since the loop completed normally without encountering `break`, the `else` block ran.

Now:

```python
for number in range(5):
    if number == 3:
        break
else:
    print("Loop completed without break")
```

Here the `else` does not run because the loop was interrupted by `break`.

This is a more advanced behavior, so I mainly want to understand the idea rather than memorize it immediately.

---

# What I Noticed

These three statements look small, but they give me more control over loops.

I can now decide:

**Should the loop stop?**

→ `break`

**Should this particular iteration be skipped?**

→ `continue`

**Do I need the block to exist, but don't want it to do anything yet?**

→ `pass`

The distinction became much clearer when I looked at them side by side.

---

# What Connected With Previous Topics?

### `for` and `while`

These statements modify the behavior of the loops I already learned.

### `if`

An `if` condition often decides when `break` or `continue` should run.

### Operators

Comparison operators help define those conditions.

### Variables

With `while` loops especially, variables determine whether repetition continues.

So these aren't completely new concepts. They are tools for controlling the behavior of concepts I already know.

---

# Practice

## Practice 1 — `break`

Print numbers from `1` to `10`, but stop when the number reaches `6`.

---

## Practice 2 — `continue`

Print numbers from `1` to `10`, but skip `5`.

---

## Practice 3 — `break` With a List

Search a list of names.

Print `"Found"` when you find `"Rahul"` and stop the loop.

---

## Practice 4 — `continue` With Numbers

Given:

```python
numbers = [10, -5, 20, -10, 30]
```

print only the positive numbers.

---

## Practice 5 — `pass`

Create a loop where you intentionally use `pass` for one particular condition.

Observe what happens compared with `continue`.

---

## Practice 6 — User Input

Create a `while True` loop that keeps asking the user for input.

Stop when they enter `"exit"`.

---

## Practice 7 — Predict the Output

Before running this code, predict what it will print:

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Then run it and compare your prediction.

---

## Practice 8 — Explain the Difference

In your own words, explain the difference between:

```python
break
continue
pass
```

This is more important than simply memorizing their definitions.

---

## My Learning Note

> `break`, `continue`, and `pass` gave me more control over loops. The main thing I need to remember is that `break` ends the loop, `continue` skips the current iteration, and `pass` simply does nothing.

---

# 03 — Control Flow: Complete

I have now covered the core Control Flow concepts:

**`if` / `elif` / `else` → decision making**

**`for` → repetition through a sequence**

**`while` → repetition based on a condition**

**`break` / `continue` / `pass` → controlling loop behavior**

These concepts will become much more powerful when I start combining them with functions and more complex problem-solving later.

---

## My Progress

```text
Decision Making
      ↓
if / elif / else
      ↓
Repetition
      ↓
for
      ↓
while
      ↓
Loop Control
      ↓
break / continue / pass
```
