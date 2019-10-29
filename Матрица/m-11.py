#  1 0 1 0 1
#  0 1 0 1 0
#  1 0 1 0 1
#  0 1 0 1 0

w = 4
l = 5
out = []
tmp = []
for i in range(w):
    if i % 2 == 0:
        for j in range(l):
            if j % 2 == 0:
                tmp.append(1)
            else:
                tmp.append(0)
    else:
        for j in range(l):
            if j % 2 == 0:
                tmp.append(0)
            else:
                tmp.append(1)
    out.append(tmp)
    tmp = []
print(out)
