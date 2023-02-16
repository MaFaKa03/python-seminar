# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# 8
# 5 4 2 2 4 2 2 5

def max_to_min(list):
    min_list = min(list)
    max_list = max(list)
    return [min_list if i == max_list else i for i in list]
print(*(max_to_min([int(i) for i in input().split()])))    