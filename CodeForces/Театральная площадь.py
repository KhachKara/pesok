# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:36:33 2019
https://codeforces.com/contest/1/problem/A
@author: khach
Театральная площадь
ограничение по времени на тест1 second
ограничение по памяти на тест256 megabytes
вводстандартный ввод
выводстандартный вывод
Театральная площадь в столице Берляндии представляет собой прямоугольник n × m метров. По случаю очередного юбилея города, было принято решение о замощении площади квадратными гранитными плитами. Каждая плита имеет размер a × a.

Какое наименьшее количество плит понадобится для замощения площади? Разрешено покрыть плитами большую поверхность, чем театральная площадь, но она должна быть покрыта обязательно. Гранитные плиты нельзя ломать или дробить, а разрешено использовать только целиком. Границы плит должны быть параллельны границам площади.

Входные данные
В первой строке записано три целых натуральных числа n, m и a (1 ≤ n, m, a ≤ 109).

Выходные данные
Выведите искомое количество плит.
"""
#input_ = [int(i) for i in input().split()]
input_ = [1001, 1000, 10]
hallSquare = input_[0] * input_[1]
plateSide = input_[2]
plateSquare = plateSide ** 2
sideA, sideB = 0, 0
if hallSquare <= plateSquare:
    plateQuantity = 1
elif input_[0] % plateSide == 0 and input_[1] % plateSide == 0:
    plateQuantity = int(hallSquare / plateSquare )
else:
    if input_[0] % plateSide == 0:
        plateQuantity = (input_[0] // plateSide) * \
                    (input_[1] // plateSide + 1)
    elif input_[1] % plateSide == 0:
        plateQuantity = (input_[0] // plateSide + 1) * \
                    (input_[1] // plateSide)
    else:
        plateQuantity = (input_[0] // plateSide + 1) * \
                    (input_[1] // plateSide + 1)
print(plateQuantity)