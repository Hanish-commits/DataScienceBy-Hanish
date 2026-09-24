# ============================================
# Break, Continue & Pass
# ============================================


# --------------------------------------------
# break
# --------------------------------------------

for number in range(1, 10):
    if number == 5:
        break

    print(number)


# break with while

number = 1

while number <= 10:
    if number == 5:
        break

    print(number)
    number += 1


# Search example

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Found!")
        break

    print(number)


# --------------------------------------------
# continue
# --------------------------------------------

for number in range(1, 6):
    if number == 3:
        continue

    print(number)


# continue with while

number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)


# --------------------------------------------
# pass
# --------------------------------------------

if True:
    pass


# pass inside a loop

for number in range(5):
    if number == 2:
        pass

    print(number)


# --------------------------------------------
# Comparing break, continue and pass
# --------------------------------------------

# break → stops the loop
for number in range(1, 6):
    if number == 3:
        break

    print(number)


# continue → skips the current iteration
for number in range(1, 6):
    if number == 3:
        continue

    print(number)


# pass → does nothing
for number in range(1, 6):
    if number == 3:
        pass

    print(number)


# --------------------------------------------
# Practical example: skip negative numbers
# --------------------------------------------

numbers = [10, -5, 20, -2, 30]

for number in numbers:
    if number < 0:
        continue

    print(number)


# --------------------------------------------
# Practical example: search for a name
# --------------------------------------------

names = ["Hanish", "Rahul", "Priya", "Aman"]

for name in names:
    if name == "Priya":
        print("Name found")
        break


# --------------------------------------------
# Practical example: while True + break
# --------------------------------------------

while True:
    command = input("Enter 'q' to quit: ")

    if command == "q":
        break

    print(f"You entered: {command}")

print("Program ended")


# --------------------------------------------
# break in nested loops
# --------------------------------------------

for row in range(3):
    for column in range(3):
        if column == 1:
            break

        print(row, column)


# --------------------------------------------
# for-else with break
# --------------------------------------------

for number in range(5):
    if number == 10:
        break
else:
    print("Loop completed without break")


for number in range(5):
    if number == 3:
        break
else:
    print("This will not be printed")