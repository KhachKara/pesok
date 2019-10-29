# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:13:43 2019
https://codeforces.com/group/DIbior3HqT/contest/255092/problem/C
@author: Karapetian
C. Переключение гравитации
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Маленький Крис скучает на занятиях по физике (слишком просто), 
поэтому он смастерил необычную коробку для игрушек, чтобы занять себя. 
Необычность коробки заключается в том, что она может изменять гравитацию!

В коробке находятся n столбиков игрушечных кубиков, расположенных в ряд: 
    i-й столбик состоит из ai кубиков. Изначально гравитация в коробке тянет 
    все кубики вниз. Когда Крис переключает гравитацию, она начинает тянуть 
    все кубики к правой стенке коробки. Рисунок показывает начальное и конечное 
    расположение кубиков в коробке: кубики, изменившие свои позиции, выделены 
    оранжевым цветом.


Вам дано изначальное расположение игрушечных кубиков в коробке. Найдите 
количество кубиков в каждом из n столбиков после переключения гравитации!

Входные данные
В первой строке входных данных записано целое число n (1 ≤ n ≤ 100), количество 
столбиков в коробке. В следующей строке записано n целых чисел через пробел: 
    i-е число ai (1 ≤ ai ≤ 100) обозначает количество кубиков в i-м столбике.

Выходные данные
Выведите n целых чисел через пробел: i-е число должно обозначать количество 
кубиков в i-м столбике после переключения гравитации.
"""
import numpy as np
input1 = 4  # input()  # 
input2 = [3, 2, 1, 2] #[int(i) for i in input().split()]  #  
maxEl = max(input2)
arr = np.zeros((maxEl, len(input2)), dtype = int)
#for i in range(maxEl):
#    for j in arr[i]:
#        arr[i,j[0]]
#        print(j)
#        break
#j = 0
#while j <= [i for i in input2]:
#    
#    j += 1
#    
j = 0
for i in range(maxEl):
    while j <= input2[i]:
        for k in arr[i,:]:
            if arr[i, k] < k:
                k = 1
            else:
                k = 0
        print(arr[i, k])