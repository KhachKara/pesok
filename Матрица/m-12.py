#  1 1 1 0 0 0 0 0 0
#  1 1 0 0 0 0 0 0 0
#  1 0 1 1 1 0 0 0 0
#  0 0 1 1 0 0 0 0 0
#  0 0 1 0 1 1 1 0 0
#  0 0 0 0 1 1 0 0 0
#  0 0 0 0 1 0 1 1 1

w = 7
l = 9
param = 3
out = []
tmp = []


def jj (list_):
    k = 0
    if len(tmp) > l - 1:
        pass
    elif i == 0:
        if k < 3:
            tmp.append(1)
            k += 1
        else:
            tmp.append(0)
    elif i % 2 != 0 and 1 not in tmp:
        k = 0
        while k < 2:
            tmp.append(1)
            k += 1
        else:
            tmp.append(0)
    elif i % 2 == 0 and 1 not in tmp:
        k = 0
        while k < 1:
            tmp.append(1)
            k += 1
    else:
        tmp.append(0)
    return tmp


for i in range(w):
    for j in range(l):
        jj(j)
    out.append(tmp)
    tmp = []
print(out)
