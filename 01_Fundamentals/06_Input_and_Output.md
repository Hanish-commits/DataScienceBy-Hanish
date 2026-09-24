# Input & Output

So far, I have mainly written programs where I provide the values directly in the code.

Now I am learning how a Python program can **receive information from a user** and then display a result.

This introduces two basic ideas:

* **Input** → getting information from the user
* **Output** → displaying information to the user

---

## Output with `print()`

I have already used `print()` to display information.

```python
print("Hello Python")
```

Output:

```text
Hello Python
```

`print()` can also display variables.

```python
name = "Hanish"

print(name)
```

Output:

```text
Hanish
```

I can also display multiple values together:

```python
name = "Hanish"
age = 30

print(name, age)
```

Output:

```text
Hanish 30
```

---

## Taking Input with `input()`

Python provides the `input()` function to get information from the user.

```python
name = input("Enter your name: ")

print(name)
```

When the program runs, Python waits for the user to enter something.

For example:

```text
Enter your name: Hanish
Hanish
```

The value entered by the user is stored in the variable `name`.

---

## Important: `input()` Returns a String

One important thing I learned is that `input()` returns the user's entry as a **string**.

For example:

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

If I enter:

```text
30
```

the output is:

```text
30
<class 'str'>
```

Even though I entered a number, Python initially treats the input as text.

This becomes important when I want to perform calculations.

---

## Taking Numeric Input

Suppose I want the user to enter their age and then add `1`.

This will not work as intended:

```python
age = input("Enter your age: ")

print(age + 1)
```

The reason is that `age` is a string.

I need to convert the input into an integer.

```python
age = int(input("Enter your age: "))

print(age + 1)
```

For example:

```text
Enter your age: 30
31
```

This combines two concepts I have already learned:

**Input → Type Conversion → Calculation → Output**

---

## Float Input

The same idea works when I need decimal numbers.

```python
price = float(input("Enter the price: "))

print(price)
print(type(price))
```

If I enter:

```text
99.50
```

Python stores it as a `float`.

---

## A Simple Input → Process → Output Flow

I am starting to see a common pattern in programs:

```text
Input
  ↓
Process
  ↓
Output
```

For example:

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(total)
```

Example:

```text
Enter price: 100
Enter quantity: 3
300.0
```

The user provides the input, Python processes it, and the program produces the output.

---

## Making Output More Readable

I can use an **f-string** to combine text and variables.

```python
name = "Hanish"
age = 30

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Hanish and I am 30 years old.
```

This makes output easier to read when I want to include variables inside a sentence.

---

## What I Noticed

`input()` helped me understand that a program does not always have to work with fixed values written inside the code.

The user can provide information while the program is running.

I also noticed an important connection between the topics I have learned so far:

**Variables → Data Types → Type Conversion → Operators → Input & Output**

These concepts are beginning to work together instead of feeling like completely separate topics.

---

## Practice

### Practice 1 — Personal Information

Ask the user for:

* name
* age
* city

Then print a sentence containing all three.

### Practice 2 — Add Two Numbers

Ask the user for two numbers and print their sum.

Remember that `input()` returns strings.

### Practice 3 — Simple Bill

Ask the user for:

* price
* quantity

Calculate the total and display it clearly.

### Practice 4 — Age Next Year

Ask the user for their current age and print their age next year.

Try these yourself before looking for a solution.

---

## My Learning Note

> Input and output made Python feel more like a real program. Until now, I was mostly giving Python values myself. Now I can let the user provide information and make the program respond to it.

---

