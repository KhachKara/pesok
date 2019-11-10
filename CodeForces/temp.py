q = int(input())
for i in range(q):
    data = list(map(int, input().split()))
    a = data[0]  # кол-во монет
    b = data[1]  # кол-во монет 1руб.
    n = data[2]  # стоимость монет
    S = data[3]  # сумма всех выбранных монет
    mod = S // n

    if S // n == 1 or a * n == S or b >= S or \
        ((S % n) * n + b >= S and n < S):
        print('YES')
    else:
        print('NO')
    
#    if [i for i in range(1, a + 1)  \
#        if i * n == S or (i * n < S and i * n + b >= S) \
#        or b >= S]:
#        print('YES')
#    else:
#        print('NO')
#4
#1 2 3 4
#1 2 3 6
#5 2 6 27
#3 3 5 18
#        10 4 3 10
