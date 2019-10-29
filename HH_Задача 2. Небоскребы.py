# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:28:20 2019

@author: Karapetian
"""

rowcol = ['col_0', 'col_1', 'col_2', 'col_3', 'col_4', 'col_5', 
          'row_6', 'row_7', 'row_8', 'row_9', 'row_10', 'row_11', 
          'col_12', 'col_13', 'col_14', 'col_15', 'col_16', 'col_17', 
          'row_18', 'row_19', 'row_20', 'row_21', 'row_22', 'row_23']

ruls = [0,0,0,2,2,0,0,0,0,6,3,0,0,4,0,0,0,0,4,4,0,3,0,0]

rulsDict = dict(zip(rowcol, ruls))

matrix = [[0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]]

rowcolDict = {
'col_0': [i[0] for i in matrix],
'col_1': [i[1] for i in matrix],
'col_2': [i[2] for i in matrix],
'col_3': [i[3] for i in matrix],
'col_4': [i[4] for i in matrix],
'col_5': [i[5] for i in matrix],

'row_6': [i[::-1] for i in matrix[0:1]],
'row_7': [i[::-1] for i in matrix[1:2]],
'row_8': [i[::-1] for i in matrix[2:3]],
'row_9': [i[::-1] for i in matrix[3:4]],
'row_10': [i[::-1] for i in matrix[4:5]],
'row_11': [i[::-1] for i in matrix[5:6]],

'col_12': [i[-1] for i in matrix[::-1]],
'col_13': [i[-2] for i in matrix[::-1]],
'col_14': [i[-3] for i in matrix[::-1]],
'col_15': [i[-4] for i in matrix[::-1]],
'col_16': [i[-5] for i in matrix[::-1]],
'col_17': [i[-6] for i in matrix[::-1]],

'row_18': [i for i in matrix[5]],
'row_19': [i for i in matrix[4]],
'row_20': [i for i in matrix[3]],
'row_21': [i for i in matrix[2]],
'row_22': [i for i in matrix[1]],
'row_23': [i for i in matrix[0]]
}

for key, value in rulsDict.items():
    if value == 6:
        for i in rowcolDict[key]:
            print(i)
A00, A01 = 5, 6
print(matrix)     