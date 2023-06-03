# Задача 26:  Напишите программу, которая на вход принимает два числа
# A и B, и возводит число А в целую степень B с помощью рекурсии.

def sqr(a, b):
    if b == 1:
        return a
    else:
        return a * sqr(a, b - 1)


print(sqr(int(input("Enter the number: ")),
          (int(input("Enter the degree of number: ")))))
