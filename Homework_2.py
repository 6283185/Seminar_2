# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число: "))
list_of_multiplication = []
res = 1
for i in range(n):
    i += 1
    res *= i
    list_of_multiplication.append(res)
print(list_of_multiplication)