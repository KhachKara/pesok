#  0 0 0 0 0
#  0 0 0 0 0
#  1 1 1 1 1
#  1 1 1 1 1

w = 4
l = 5
out = []
tmp = []
for i in range(w):
    for j in range(l):
        if i <= 1:
            tmp.append(0)
        else:
            tmp.append(1)
    out.append(tmp)
    tmp = []
print(out)