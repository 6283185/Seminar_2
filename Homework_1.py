# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

a = input("Введите вещественное число: ").split(".")

b = int(a[0]) # целая часть числа 
c = int(a[1]) # дробная часть

sum = 0
while b != 0:
    sum += b % 10
    b = b // 10
    
while c != 0:
    sum += c % 10
    c //= 10
    
    
print(sum)