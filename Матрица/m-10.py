#  1 1 0 0 0
#  0 1 1 0 0
#  0 0 1 1 0
#  0 0 0 1 1

w = 4
l = 5
out = []
tmp = []
k = 0
for i in range(w):
    for j in range(l):
        if j == k or j == k + 1:
            tmp.append(1)
        else:
            tmp.append(0)
    k += 1
    out.append(tmp)
    tmp = []
print(out)
