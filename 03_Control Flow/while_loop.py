# ============================================
# While Loops
# ============================================

# Basic while loop

count = 1

while count <= 5:
    print(count)
    count += 1


# Counting backwards

count = 5

while count >= 1:
    print(count)
    count -= 1


# User input

number = int(input("Enter a positive number: "))

while number <= 0:
    number = int(input("Please enter a positive number: "))

print(f"You entered {number}")


# while with if

number = 1

while number <= 10:
    if number % 2 == 0:
        print(number)

    number += 1


# Accumulating a result

number = 1
total = 0

while number <= 5:
    total = total + number
    number += 1

print(total)


# Boolean variable

running = True

while running:
    print("Program is running")
    running = False


# while True

# This is intentionally an infinite loop.
# It should normally be combined with break.

# while True:
#     print("This keeps running")


# Password example

password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")


# Menu-style example

choice = ""

while choice != "q":
    print("Enter q to quit")
    choice = input("Your choice: ")

print("Program ended")


# while loop with else

count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed")


# Same task with for loop

for number in range(1, 6):
    print(number)


# Same task with while loop

number = 1

while number <= 5:
    print(number)
    number += 1