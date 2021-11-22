def evklid(a, b):
    """
    Алгоритм Евклида для быстрого вычисления НОД
    """
    if b == 0: 
           return a
    return evklid(b, a % b)