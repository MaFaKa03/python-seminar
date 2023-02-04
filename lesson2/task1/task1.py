#Сдвиг массива налево на =к шагов

list_nums = [1, 2, 3, 4, 5]
k = 7
print(list_nums)
result = list_nums[(k % len(list_nums)):] + list_nums[:(k % len(list_nums))]
print(result)

# list_nums = [1, 2, 3, 4, 5]
# k = 7

# print(list_nums)

# for i in range(k - 1):
#     list_nums.insert(0, list_nums.pop(- 1))

# print(k, list_nums)