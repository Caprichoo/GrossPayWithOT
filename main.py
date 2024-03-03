print('**Welcome to Gross Pay with Overtime**')
hours = float(input('Enter number of hours:'))
rate = float(input('Enter rate: '))
pay = float(hours * rate)
if hours > 40:
    pay = (hours - 40) * rate * 1.5 + 40 * rate  #PEMDAS
    print(f'Your Overtime pay is: {pay}')
else:
    print(f'Your pay without Overtime is: {pay}')
