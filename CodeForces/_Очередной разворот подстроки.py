# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:12:32 2019
https://codeforces.com/problemset/problem/1234/F
@author: Karapetian
Очередной разворот подстроки
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Вам задана строка s, состоящая только из первых 20 строчных букв латинского алфавита ('a', 'b', ..., 't').
Напомним, что подстрокой s[l;r] строки s называется строка slsl+1…sr. Например, подстроками «codeforces» являются «code», «force», «f», «for», но не строки «coder» и «top».
Вы можете произвести следующую операцию не более одного раза: выбрать какую-то подстроку s[l;r] и развернуть ее (то есть строка slsl+1…sr превращается в srsr−1…sl).
Ваша задача — максимизировать длину максимальной подстроки s, состоящей из различных (то есть уникальных) символов.
Строка состоит из различных символов, если ни один символ этой строки не встречается более одного раза. Например, строки «abcde», «arctg» и «minecraft» состоят из различных символов, а строки «codeforces», «abacaba» не состоят из различных символов.
Входные данные
Единственная строка входных данных содержит одну строку s, состоящую из не более, чем 106 символов 'a', 'b', ..., 't' (первых 20 строчных букв латинского алфавита).
Выходные данные
Выведите одно целое число — максимально возможную длину максимальной подстроки s, состоящей из различных символов, после переворота не более чем одной ее подстроки.
"""

ableLetters = 'abcdefghijklmnopqrst'
# input_ = [j for j in input() if j in ableLetters]
input_ = list('boodbpmpdfrmackcrtbasatcjbbbgkkrcdmiejqpqiqqpfepinqscfcrhglqnqnehsrmljoqdtsboammreagilegamlforqsknbn')

maxLength = 0
j = 0
out = []
while j <= len(input_):
    for i in input_:
        if i in out:
            if len(out) > maxLength:
                temp =
                maxLength = len(out)
                out = []
                pass
        else:
            out.append(i)
    j += 1
print(maxLength)


"""
def checkmaxlength(someList):
    maxLength = 0
    j = 0
    out = []
    while j <= len(someList):
        for i in someList:
            if i in out:
                if len(out) > maxLength:
                    maxLength = len(out)
                    out = []
                    pass
            else:
                out.append(i)
        j += 1
    return len(out)
"""