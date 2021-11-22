"""
Бинарное возведение в степень
Бинарное (двоичное) возведение в степень — это приём, 
позволяющий возводить любое число в n-ую степень за O(\log n) умножений 
(вместо n умножений при обычном подходе).
"""

def binpow (a: int, n: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 1:
        return binpow(a, n - 1) * a
    else:
        b = binpow(a, n / 2)
        return b * b

if __name__ == '__main__':
    print(binpow(int(input()), int(input())))