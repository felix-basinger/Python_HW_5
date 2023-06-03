# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую
# сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя
# использовать циклы.

def summ(a, b):
    if a < 0 or b < 0:
        return
    else:
        if b == 0:
            return a
        else:
            return 1 + summ(a, b - 1)


print(summ((int(input("Enter the 1 number: "))), (int(input("Enter the 2 number: ")))))
