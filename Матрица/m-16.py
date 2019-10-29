#  1 1 1 0 0 0 0 0 0
#  1 1 0 0 0 0 0 0 0
#  1 0 0 0 0 0 0 0 0
#  0 0 0 1 1 1 0 0 0
#  0 0 0 1 1 0 0 0 0
#  0 0 0 1 0 0 0 0 0
#  0 0 0 0 0 0 1 1 1
#  0 0 0 0 0 0 1 1 0
#  0 0 0 0 0 0 1 0 0

import numpy as np
parameter = 3
zeros = np.zeros((parameter, parameter), dtype=int)


def draw_1():
    out = []
    tmp = []
    for i in range(parameter):
        for j in range(parameter):
            tmp.append(0)
            if i + j <= parameter-1:
                tmp[j] = 1
            else:
                tmp[j] = 0
        out.append(tmp)
        tmp = []
    return out


w = 9
l = 9
z = np.array(draw_1())
out_ = []
print(np.concatenate((z, zeros, zeros), axis=1))
print(np.concatenate((zeros, z, zeros), axis=1))
print(np.concatenate((zeros, zeros, z), axis=1))
