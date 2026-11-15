# Exercise 3: Check whether a Gregorian year is a leap year

year = int(input("Enter a Gregorian year: "))

if year <= 0:
    print("Invalid year.")
elif year % 400 == 0:
    print("This is a leap year.")
elif year % 100 == 0:
    print("This is not a leap year.")
elif year % 4 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")
