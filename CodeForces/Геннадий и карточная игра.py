input1 = input()
input2 = input().split()
if input1[0] in [i[0] for i in input2] or input1[1] in [i[1] for i in input2]:
    print('YES')
else:
    print('NO')