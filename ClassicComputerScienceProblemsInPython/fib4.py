from functools import lru_cache

@ lru_cache (maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


if __name__ == "__main__":
    print(fib4(int(input("Введите число: "))))