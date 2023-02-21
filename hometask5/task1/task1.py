# Задача 32: Определить индексы элементов массива (списка),
#  значения которых принадлежат заданному диапазону ()
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# 5
# 15
# [1, 9, 13, 14, 19]

from random import randint
list_numbers = []
for i in range(int(input("Enter size list: "))):
    list_numbers.append(randint(-10, 20))
print(list_numbers)
min = int(input("Enter min horizone: "))
max = int(input("Enter max horizone: "))
print([ind for ind, val in enumerate(list_numbers) if min <= val <= max])




