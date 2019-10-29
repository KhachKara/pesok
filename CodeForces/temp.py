# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:58:30 2019

@author: khach
"""
import numpy as np
input2 = [3, 2, 1, 2]
maxElement = max(input2)
length = len(input2)
arr = []
tmp = []
out = []
numArray = np.zeros((maxElement, len(input2)), dtype=int)


for i in range(maxElement):
    for j in range(len(input2)):
        if input2[j] > 0:
            tmp.append(1)
        else: 
            tmp.append(0)
        input2[j] -= 1
    arr.append(tmp)
    tmp = []
c = numArray + arr
# for i in c:
#     out.append(sorted(i))
# k =1
# for i in out:
#     print(i[len(i)-k])
#     k += 1
