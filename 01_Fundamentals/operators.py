# Python Operators

# Arithmetic Operators

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# Assignment Operators

score = 100

score += 10
print(score)

score -= 20
print(score)

score *= 2
print(score)


# Comparison Operators

age = 25

print(age == 25)
print(age != 30)
print(age > 18)
print(age < 18)
print(age >= 25)
print(age <= 20)


# Logical Operators

is_adult = True
is_learning = True

print(is_adult and is_learning)
print(is_adult or is_learning)
print(not is_learning)


# Operator Precedence

result = 10 + 5 * 2
print(result)

result = (10 + 5) * 2
print(result)


# Practical Example

price = 500
quantity = 3
discount = 100

total = price * quantity
final_price = total - discount

print(final_price)