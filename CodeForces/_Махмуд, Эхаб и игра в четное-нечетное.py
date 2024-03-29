# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:33:30 2019
https://codeforces.com/problemset/problem/959/A
@author: khach
Махмуд, Эхаб и игра в четное-нечетное
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Махмуд и Эхаб играют в игру, которую они называют игрой в четное-нечетное. Эхаб выбирает его любимое положительное целое число n, после чего они ходят по очереди. Первый ход делает Махмуд. Каждый игрок в свой ход должен уменьшить n на целое число a, выбранное этим игроком, такое, что:

1 ≤ a ≤ n.
Если ходит Махмуд, a должно быть чётным, а если ходит Эхаб, a должно быть нечётным.
Если игрок в свой ход не может выбрать число, удовлетворяющее данным условиям, он проигрывает игру. Определите, кто выиграет при оптимальной игре обоих игроков.

Входные данные
В единственной строке находится целое число n (1 ≤ n ≤ 109) — число, выбранное Эхабом в начале игры.

Выходные данные
Выведите «Mahmoud» (без кавычек), если победит Махмуд и «Ehab» (без кавычек) в противном случае.
"""
input_ = int(input())

