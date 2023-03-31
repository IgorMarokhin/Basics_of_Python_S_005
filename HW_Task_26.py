'''
Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

def raise_number_to_power(A: int, B: int) -> int:
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        return A * raise_number_to_power(A, B - 1)

def main() -> None:
    A = int(input('Введите основание степени: '))
    B = int(input('Введите показатель степени: '))
    power_of_number = raise_number_to_power(A, B)
    print(f'A = {A}; B = {B} -> {power_of_number}')

if __name__ == '__main__':
    main()