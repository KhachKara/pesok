#  1 1 1 1 1
#  0 1 1 1 1
#  0 0 1 1 1
#  0 0 0 1 1

w = 4
l = 5
out = []
tmp = []
k = 0
for i in range(w):
    for j in range(l):
        tmp.append(1)
        if len(tmp) >= l:
            break

    out.append(tmp)
    tmp = []
    k += 1
    m = 0
    while m < k:
        tmp.append(0)
        m += 1

print(out)
