#  0 1 0 1 0
#  0 1 0 1 0
#  0 1 0 1 0
#  0 1 0 1 0

w = 4
l = 5
out = []
tmp = []
for i in range(w):
    for j in range(l):
        if j % 2 != 0:
            tmp.append(1)
        else:
            tmp.append(0)
    out.append(tmp)
    tmp = []
print(out)
