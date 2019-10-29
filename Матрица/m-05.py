#  0 1 1 1 1
#  0 0 1 1 1
#  0 0 0 1 1
#  0 0 0 0 1

w = 4
l = 5
out = []
tmp = []
k = 1
for i in range(w):
    m = 0
    while m < k:
        tmp.append(0)
        m += 1
    for j in range(l):
        tmp.append(1)
        if len(tmp) >= l:
            break

    out.append(tmp)
    tmp = []
    k += 1


print(out)
