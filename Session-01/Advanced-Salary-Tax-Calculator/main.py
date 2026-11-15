
salary = int(input("Enter your salary: "))

if salary <= 10000000:
    tax = 0

elif salary <= 25000000:
    tax = (salary - 10000000) * 0.10

else:
    tax = 1500000 + (salary - 25000000) * 0.20

child = input("Does the employee have a child? (yes/no): ")

if child == "yes":
    tax = tax - 500000

print("Final tax:", tax, "Toman")
