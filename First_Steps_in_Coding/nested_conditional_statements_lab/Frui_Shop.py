fruit = input()
day_of_week = input()
count = float(input())
price = 0

if day_of_week in ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday']:
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
    total = price * count
    if total != 0:
        print(f'{total:.2f}')
    else:
        print('error')

elif day_of_week in ['Saturday', 'Sunday']:
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    total = price * count
    if total != 0:
        print(f'{total:.2f}')
    else:
        print('error')
else:
    print('error')


