# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# 1 2 3 4 5 6 7 8 9 10 11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

a = int(input("Enter number: "))
start = 0
finish = 1
count = 2
while finish <= a:
    if a == finish:
       print(count)
       break
    start, finish = finish, start + finish
    count += 1    
else: print("-1")
