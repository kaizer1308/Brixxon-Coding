import os
os.system("cls")

# Exercise: hours worked function

def gross_pay():
    hrs_worked = float(input("Enter hours worked: "))
    rate = float(input("Enter rate per hour: "))
    pay = hrs_worked * rate
    print("Gross pay =", pay)
    
    print("Employee 1:")
gross_pay()
print("Employee 2:")
gross_pay()    