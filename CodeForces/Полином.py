# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 02:02:30 2019
https://codeforces.com/group/DIbior3HqT/contest/259870/problem/D
@author: khach
Полином
ограничение по времени на тест1 секунда
ограничение по памяти на тест64 мегабайта
вводстандартный ввод
выводстандартный вывод
Необходимо вычислить значение полинома a0 + a1X + a2X2 + a3X3 + ... + aNXN при заданном X.

Входные данные
В первой строке записано два числа N и X (0<=N<=105, 1<=X<=109).

Во второй строке записано N+1 число a0,a1,a2,...aN (1<=ai<=109).

Выходные данные
Выведите ответ по модулю 109 + 7.
"""

N, X = map(int, input().split())
(i for i in range(N + 1)) = map(int, input().split())
res = sum([i * X ** i for i in range(N + 1)])
print(res)