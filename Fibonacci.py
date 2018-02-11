from functools import lru_cache
# lru_cache - List Recently Used Cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check that the input is an integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n - 2)


# fibonacci(2.1)

# for n in range(1, 501):
#     print(n, ":", fibonacci(n))


for n in range(1, 51):
    print(fibonacci(n+1) / fibonacci(n))

# Golden ratio 1.618033988749895


# fibonacci_cache = {}
#
#
# def fibonacci(n):
#     # If we have cached the value, then return it
#     global value
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#
#     # Compute the Nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n - 2)
#
#     # Cache the value and return it
#     fibonacci_cache[n] = value
#     return value
#
#
# for n in range(1, 101):
#     print(n, ":", fibonacci(n))


# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n - 2)
#
#
# for n in range(1, 11):
#     print(n, ":", fibonacci(n))
