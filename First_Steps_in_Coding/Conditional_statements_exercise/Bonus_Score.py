number = int(input())
bonus = 0

if number <= 100:
    bonus = 5

elif number <= 1000:
    bonus = 0.2 * number

else:
    bonus = 0.1 * number

if number % 2 == 0:
    bonus = 1 + bonus

if number % 10 == 5:
    bonus = 2 + bonus

print(bonus)
print(bonus + number)