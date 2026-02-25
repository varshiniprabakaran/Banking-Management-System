salary = int(input("Enter your salary: "))
tax = 0

if salary <= 300000:
    tax = 0
elif salary <= 700000:
    tax = salary * 0.10
else:
    tax = salary * 0.20
    
print("Tax:", tax)
