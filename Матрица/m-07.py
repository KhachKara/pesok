#  0 0 0 0 1
#  0 0 0 1 1
#  0 0 1 1 1
#  0 1 1 1 1

w = 4
l = 5
out = []
tmp = []
k = l
m = 0
for i in range(w):
    m += 1
    for j in range(l):
        if len(tmp) + m >= l:
            tmp.append(1)
        else:
            tmp.append(0)
    out.append(tmp)
    tmp = []
print(out)
