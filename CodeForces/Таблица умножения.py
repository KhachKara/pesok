# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:42:50 2019
https://codeforces.com/group/DIbior3HqT/contest/254437/problem/E
@author: khach
Таблица умножения
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Рассмотрим таблицу из n строк и n столбцов. Известно, что в клетке, образованной пересечением i-й строки и j-го столбца, записано число i × j. Строки и столбцы нумеруются с единицы.

Дано целое положительное число x. Требуется посчитать количество клеток таблицы, в которых находится число x.

Входные данные
В единственной строке находятся числа n и x (1 ≤ n ≤ 105, 1 ≤ x ≤ 109) — размер таблицы и число, которое мы ищем в таблице.

Выходные данные
Выведите единственное число: количество раз, которое число x встречается в таблице.
"""
input_ = [int(i) for i in input().split()]
n = input_[0]
x = input_[1]
out = []
res = 0
for i in range(1, n+1):
    if x % i == 0:
        divigion = x // i
        if divigion <= x:
            out.append(divigion)
for k in list(set(out)):
    for j in list(set(out)):
        if k * j == x:
            res += 1
        
print(res)