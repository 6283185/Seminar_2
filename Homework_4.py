# 4. Задайте список из N элементов, заполненных числами
#  из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. 
# Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
n = int(input("Введите число: "))
a = [int(i) for i in input("Введите индексы требуемых элементов списка через пробел: ").split()]
n_list = []
n = - n
for i in range(abs(n) * 2 + 1): # т.к. строкой выше присвоил n отрицательное значение взял по модулю и добавил 1 для нуля
    n_list.append(n)
    n += 1
multiply = 1
for j in a:
    multiply *= n_list[j]

print(f"Произведение чисел из списка {n_list} под индексами {a} = {multiply}")