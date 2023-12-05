# import functools
# @functools.lru_cache(None)
# def f(n):
#     if n > 2024:
#         return n
#     if n <= 2024:
#         return n * f(n + 1)
#
# print(f(2022) / f(2024))

# def f(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return n + f(n - 1)
#     if n % 2 != 0 and n > 1:
#         return 2 * f(n - 2)
# print(f(26))

# def f(n):
#     if n > 2 : return f(n - 1) * f(n - 3)
#     if n == 0: return 1
#     if n == 1: return 3
#     if n == 2: return 2
#
# print(f(7))
# def g(n):
#     if n > 40: return 10
#     if n < 41: return 30 + f(n + 600 // n)
#
# def f(n):
#     if n < 50: return n
#     if n > 49: return 2 * g(50 - n // 2)
# print(f(80))

# def f(n):
#     if n <= 3: return n
#     if 3 < n <= 32: return n // 4 + f(n - 3)
#     if n > 32: return 2 * f(n - 5)
# print(f(100))

# import functools, sys
# sys.setrecursionlimit(9999)
#
# @functools.lru_cache(None)
# def f(n):
#     if n < 3: return 2
#     if n > 2: return 2*f(n-2)
#
# print(f(2222) / f(2182))

# import functools, sys
# sys.setrecursionlimit(9999)
#
# @functools.lru_cache(None)
# def f(n):
#     if n < 3: return n + 1
#     if n >= 3 and n % 2 == 0: return f(n - 2) + n - 2
#     if n >= 3 and n % 2 != 0: return f(n + 2) + n + 2
# k = 0
# n = 1
# while True:
#     if 9999 < f(n) <= 99999:
#         k += 1
#     n += 1
# print(f(3))

# import functools, sys
# sys.setrecursionlimit(9999)
#
# @functools.lru_cache(None)
# def h(x):
#     if x >= 4040: return x
#     if x < 4040: return x + 4 + h(x + 4)
# print(h(3) - h(15))

import functools, sys
# sys.setrecursionlimit(9999)

@functools.lru_cache()
def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n - 1)
print((f(2023) - f(2022)) / f(2020))