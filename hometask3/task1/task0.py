# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#  m - кол-во элементов второго множества.
#  Затем пользователь вводит сами элементы множеств

n = int(input())
first_set = set()
while len(first_set) < n:
    first_set.add(int(input()))
print(first_set)

m = int(input())
second_set = set()
while len(second_set) < n:
    second_set.add(int(input()))
print(second_set)

i = first_set.intersection(second_set)

print(i)
