# Exercise 1: Check Whether a Number Is Positive, Negative, Zero, Even, or Odd
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")