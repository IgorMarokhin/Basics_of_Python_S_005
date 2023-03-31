'''
Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом 0.
Определите значение второго по величине элемента в этой последовательности, то есть элемента,
который будет наибольшим, если из последовательности удалить наибольший элемент.
В этой задаче нельзя использовать глобальные переменные.
Функция получает данные, считывая их с клавиатуры, а не получая их в виде параметра.
В программе на языке Python функция возвращает результат в виде кортежа из нескольких чисел
и функция вообще не получает никаких параметров. В программе на языке C++ результат записывается
в переменные, которые передаются в функцию по ссылке. Других параметров, кроме как используемых
для возврата значения, функция не получает.
Гарантируется, что последовательность содержит хотя бы два числа (кроме нуля).
1 3 5 7 3 6 8 4 3 2 0 -> 7
1 2 3 4 5 6 3 1 2 5 3 -> 5
'''

def get_second_biggest_number() -> tuple:
    current_number = None
    counter = 1
    sequence = list()
    while current_number != 0:
        current_number = int(input(f'Введите {counter} число последовательности: '))
        sequence.append(current_number)
        counter += 1

    first_biggest_index = max(sequence)
    temp_sequence = sequence[:]
    while first_biggest_index in temp_sequence:
        temp_sequence.remove(first_biggest_index)

    return *sequence, max(temp_sequence)


def main():
    *sequence, second_biggest = get_second_biggest_number()
    print(f'Второе по величине число в последовательности {sequence} -> {second_biggest}')


if __name__ == '__main__':
    main()