# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:41:12 2019

@author: khach

Counting Valleys
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    L=0
    V=0
    for i in s:
        if i == 'U':
            L += 1
            if L == 0:
                V += 1
        else:
            L -= 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
