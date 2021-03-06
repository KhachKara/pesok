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
Как известно, нет самолетов-мужчин и самолетов-женщин. Однако, 
каждому самолету на Земле нравится какой-то один другой самолет. 
Всего на Земле n самолетов, пронумерованных от 1 до n, 
при этом самолету номер i нравится самолет fi, где 1 ≤ fi ≤ n, 
а также fi ≠ i.

Назовем любовным треугольником ситуацию, 
когда самолету A нравится самолет B, самолету B нравится самолет C, 
а самолету C нравится самолет A. Проверьте, 
есть ли на Земле хотя бы один любовный треугольник.
"""
# input1 = input()
# input2 = [int(i) for i in input().split()]
input1 = 5
#         1  2  3  4  5  6  7  8  9  10 11 12
input2 = [3, 6, 6, 5, 4, 8, 5, 2, 5, 3, 2, 4]  # [2, 4, 5, 1, 3]  # [5, 5, 5, 5, 1] # 
for j in range(1, len(input2)+1):      
    step1 = input2[j-1]
    step2 = input2[step1-1]
    step3 = input2[step2-1]
    if input2[step3-1] == step1:
        print(step1, step2, step3)
        print('YES')
        break
else:
    print('NO')