# Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.

def degree(a, b):
    #c = a * a
    if b == 0:
        return a
    if b < 0:
        return degree(a, b + 1) * 1 / a
    #while b > 0:
    else:    
        return degree(a, b - 1) * a
print(degree(int(input()), int(input())))                