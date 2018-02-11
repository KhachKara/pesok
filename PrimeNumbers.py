"""Программа выводит все простые числа в заданном диапазоне n"""
a = []
try:
    n = int(input("n="))
    for i in range(n+1):
        a.append(i)
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    print(lst)
except ValueError:
    print("Введите корректное число")
except IndexError:
    print("Введите корректное число")
