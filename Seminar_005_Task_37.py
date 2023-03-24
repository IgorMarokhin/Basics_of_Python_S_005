'''
Задача No37. Решение в группах
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4 Output: 4 3
'''

def recursive_input2(size_n: int):
    x = input('please input: ')
    if size_n == 1:
        print(x, end=' ')
    else:
        recursive_input2(size_n - 1)
        print(x, end=' ')

n = int(input('Please input number: '))

recursive_input2(n)