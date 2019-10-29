#  0 0 0 0 0
#  0 0 0 0 0
#  0 0 0 0 0
#  0 0 0 0 0

w = 4
l = 5
out = []
tmp = []
for i in range(w):
    for j in range(l):
        tmp.append(0)
    out.append(tmp)
    tmp = []
print(out)
