'''
Задача No31. Решение в группах
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи.

Input: 7 Output: 21
Задание необходимо решать через рекурсию
'''

n1 = int(input("Введите искомый элемент: "))
def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(0, n1 + 1):
    list_1.append(fib(i))
print(*list_1)

print(list_1[n1])

num = int(input('Please input number: '))


def fibonachy(n: int):
    if n == 0 or n == 1:
        return n
    return fibonachy(n - 1) + fibonachy(n - 2)


print(fibonachy(num))