# 5. Реализуйте алгоритм перемешивания списка.
import random 
from random import Random, randint 

# Через shuffle:

# a = [i for i in input("Заполните список элементами через пробел: ").split()]
# # список в виде строки, так что можно любыми элементами заполнить
# print("Изначальный список: ",a)
# random.shuffle(a)
# print("Перемешанный список: ", a)

# алгоритм:

a = [i for i in input("Заполните список элементами через пробел: ").split()]
# список в виде строки, так что можно любыми элементами заполнить
print("Изначальный список: ",a)
for i in range(len(a)):
    index = randint(0, len(a) - 1)
    temp = a[i]
    a[i] = a[index]
    a[index] = temp
print("Перемешанный список: ", a)
