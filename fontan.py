arr = [0, 0, 2, 0, 0, 0, 0, 3]  # , 1, 2, 1, 5, 0, 1, 0, 0, 1, 2, 3, 0]  # 4
mem = []
tpl = []
fontan = 0
coverValue = [0, 1]  # (индекс, значение)
for i in range(len(arr)):
    tpl.append(tuple([i + 1, arr[i]]))
j = 1
flag = False
for i in tpl:
    coverValue[0] = i[0]
    if j >= coverValue[1] and flag == False: 
        fontan += 1
    else:
        j += 1
    if j > coverValue[1]:
        flag = False
    if i[1] != 0:
        mem.append([i[0], i[1]])
        coverValue[1] = i[1]
        fontan = fontan - coverValue[1]
        flag = True

print(mem)
