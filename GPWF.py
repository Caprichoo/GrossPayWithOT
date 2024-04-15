print("**Welcome to Gross Pay Calculator done with functions**")
def gross_pay(hours, rate):
    if hours < 40:
        pay = round(rate * hours, 2)
    else:
        overtime = hours - 40
        pay = (rate * 40) + (1.5 * rate * overtime)
        return pay

hours = float(input("Enter number of hours: "))
rate = float(input("Enter rate: "))

print(gross_pay(hours, rate))

