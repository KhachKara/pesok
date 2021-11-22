from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # 
    if n > 0: yield 1
    last: int = 0  # специальный случай
    next: int = 1  # начальное значение fib(0)
    
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # главный этап генерации
    
if __name__ == "__main__":
    for i in fib6(int(input("Введите число: "))):
        print(i)