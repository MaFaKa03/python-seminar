# 2 Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

nums = [randint(1, 10) for _ in range(int(input()))]
print(nums)

find_num = int(input())
num_x = nums[0]

for i in nums:
    if abs(find_num - i) < abs(find_num - num_x):
        num_x = i
print(num_x)            