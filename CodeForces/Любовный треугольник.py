# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:06:43 2019
https://codeforces.com/group/DIbior3HqT/contest/255092/problem/B
@author: Karapetian
Любовный треугольник
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Как известно, нет самолетов-мужчин и самолетов-женщин. Однако, каждому самолету на Земле нравится какой-то один другой самолет. Всего на Земле n самолетов, пронумерованных от 1 до n, при этом самолету номер i нравится самолет fi, где 1 ≤ fi ≤ n, а также fi ≠ i.

Назовем любовным треугольником ситуацию, когда самолету A нравится самолет B, самолету B нравится самолет C, а самолету C нравится самолет A. Проверьте, есть ли на Земле хотя бы один любовный треугольник.
"""
# input1 = input()
# input2 = [int(i) for i in input().split()]

#
# def lover(ind):
#     return dict_[ind]


input1 = 5
input2 = [5, 6, 6, 3, 2, 5, 5, 2, 5, 3, 2, 4]  # [2, 4, 5, 1, 3]
indexes = [i for i in range(1, len(input2) + 1)]
lovers = []
dict_ = dict(zip(indexes, input2))
ind = 1
k = 0
j = 0
while j <= len(input2):
    print(dict_[ind])
    if dict_[ind] not in lovers:
        lovers.append(dict_[ind])
        ind = dict_[ind]
        if dict_[ind] == lovers[0] and len(lovers) == 3:
            break
    if k >= 3:
        break
    k += 1
    j += 1
if len(lovers) == 3 and dict_[ind] == lovers[0]:
    print('YES')
else:
    print('NO')
