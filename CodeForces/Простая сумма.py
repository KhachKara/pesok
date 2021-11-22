# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:16:09 2019
https://codeforces.com/group/DIbior3HqT/contest/258122/problem/B
@author: Karapetian
Простая сумма
ограничение по времени на тест1.5 секунд
ограничение по памяти на тест512 мегабайт
вводстандартный ввод
выводстандартный вывод
Вам дано Q запросов.

Запрос состоит из двух чисел L и R, ответом на запрос будет являться сумма простых чисел на отрезке [L, R].

Входные данные
В первой строке дано натуральное число Q (Q ≤ 100).

В каждой из последующих Q строк записано по два натуральных числа L и R (1 ≤ L ≤ R ≤ 3·107) для каждого запроса.

Выходные данные
В каждой из Q строк выведите ответ на соответствующий запрос.
"""


def simple_nums1(n):
    """
    Простые числа
    Решение за O(n): перебираем все числа от 2 до n-1 и проверяем, делится ли на них n.
    Если делится – n составное, иначе простое.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


Q = int(input())

out = [None] * Q
for j in range(Q):
    res = 0
    nums = [i for i in [int(j) for j in input().split()]]
    for k in range(nums[0], nums[-1] + 1):
        if simple_nums1(k):
            res += k
            print(res)
    out[j] = res 
for z in out:
    print(z)