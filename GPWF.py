print("**Welcome to Gross Pay Calculator done with functions**")
def gross_pay(hours, rate):
    if hours < 40:
        pay = round(rate * hours, 2)
    else:
        overtime = hours - 40
        pay = (rate * 40) + (1.5 * rate * overtime)
        return pay


def check_for_input(u_input):
    try:
        val = float(u_input)
        return val
    except:
        print("Error, Please enter numeric value")
        quit()


hours = float(input("Enter number of hours:"))
print(check_for_input(hours))
rate = float(input("Enter rate: "))
print(check_for_input(rate))

print(gross_pay(hours, rate))

