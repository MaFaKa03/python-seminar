# Дано натуральное число N и последовательность
# из N элементов. Требуется вывести эту
# последовательность в обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать
# циклы (даже для ввода и вывода).

def rev_num(num):
    if num == 0:
        return ""
    nums = input()
    return rev_num(num - 1) + f"{nums} "


print(rev_num(int(input())))
