'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*
2 + 2 = 4
'''

def sum_integer(A: int, B: int) -> int:
    if A:
        return 1 + sum_integer(A - 1, B)
    elif B:
        return 1 + sum_integer(A, B - 1)
    else:
        return 0

def main() -> None:
    A = int(input('Введите первое целое число: '))
    B = int(input('Введите второе целое число: '))
    sum_of_integer = sum_integer(A, B)
    print(f'{A} + {B} = {sum_of_integer}')

if __name__ == '__main__':
    main()