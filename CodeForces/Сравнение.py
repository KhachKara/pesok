# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:10:40 2019
https://codeforces.com/group/DIbior3HqT/contest/259870/problem/C
@author: Karapetian
Сравнение
ограничение по времени на тест1 секунда
ограничение по памяти на тест64 мегабайта
вводстандартный ввод
выводстандартный вывод
Вам необходимо сравнить лексикографически две строки.

Входные данные
Даны две строки a и b, каждая из которых содержит только латинские буквы и цифры. Длина каждой строки не превышает 106 символов.

Выходные данные
Выведите символ меньше (‘<’), если строка a меньше строки b, символ равно (‘=’), если они равны и символ больше (‘>’), если строка a больше строки b.
"""
res1 = 0; res2 = 0
a = input()
b = input()
res1 = sum([ord(i) for i in a])
res2 = sum([ord(i) for i in b])
if res1 < res2:
    print('<')
elif res1 > res2:
    print('>')
else:
    print('=')
