# 2. Для натурального n создать последовательность (3*n + 1).
# *Пример:*
# - Для n = 6: 4, 7, 10, 13, 16, 19

n = int(input("Введите число: "))
i = 1

while i <= n:
    print(3 * i + 1, end = " ")
    i += 1
    