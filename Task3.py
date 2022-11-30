# 3. Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество 
# вхождений одной строки в другой.
# 'Я люблю Python'
# 'лю'
# --> 2

first_string = input("Введите строку: ")
second_string = input("Введите строку: ")


res = first_string.count(second_string)
print(f"Количество вхождений второй строки в первую = {res}")

# list = text.split(searchText) # через сплит и считает количество кусков после разделения
# print(len(list)-1)

# count = 0 
# for i in range(len(first_string) - len(second_string)+1):
#     if first_string[i:i+len(second_string)] == second_string:
#         count += 1
# print(f"Количество вхождений второй строки в первую = {count}")