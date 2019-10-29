#  1 0 0 0 0
#  0 1 0 0 0
#  0 0 1 0 0
#  0 0 0 1 0

w = 4
l = 5
out = []
tmp = []
k = 0
for i in range(w):
    for j in range(l):
        tmp.append(0)
    tmp[k] = 1
    out.append(tmp)
    tmp = []
    k += 1
print(out)
