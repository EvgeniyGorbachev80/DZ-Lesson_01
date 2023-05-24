# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


number = int(input('Введите трехзначное число: '))
while number // 1000 > 0 :   
    if number // 1000 > 0:
        print('Число не трехзначное')
        number = int(input('Введите трехзначное число: '))

summa = 0
while number > 0:
    x = number % 10
    summa = summa + x
    number = number // 10

print(f'Сумма цифр трехзначного числа равна: {summa}')