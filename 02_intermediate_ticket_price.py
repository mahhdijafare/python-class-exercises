
# Exercise 2: Movie Ticket Pricing Based on Age

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age < 5:
    print("The ticket is free.")
elif age < 18:
    print("Ticket price: 50,000 tomans")
elif age <= 60:
    print("Ticket price: 100,000 tomans")
else:
    print("Ticket price: 70,000 tomans")
