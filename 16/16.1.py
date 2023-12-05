# def f(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return n + f(n - 1)
#     if n > 1 and n != 2:
#         return 2 * f(n - 2)
#
# print(f(26))

# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     if n > 1:
#         return 3 * f(n - 1) - f(n - 2)
#
# print(f(6))

# def f(n):
#     if n == 0: return 1
#     if n == 1: return 3
#     if n == 2: return 2
#     if n > 2:
#         return f(n - 1) * f(n - 3)
#
# print(f(7))

# def f(n):
#     if n < 50:
#         return n
#     if n > 49:
#         return 2 * g(50 - n // 2)
# def g(n):
#     if n > 40:
#         return 10
#     if n < 41:
#         return 30 + f(n + 600 // n)
#
# print(f(80))


import functools


# @functools.lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) - 2 * g(n - 1)
#
# @functools.lru_cache(None)
# def g(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) + g(n - 1) + n
#
# print(sum(map(int, str(g(36)))))

# @functools.lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) + 3 * g(n - 1)
#
# @functools.lru_cache(None)
# def g(n):
#     if n == 1: return 1
#     if n > 1:
#         return f(n - 1) - 2 * g(n - 1)
#
# print(sum(map(int, str(f(18)))))

# def f(n):
#     if n <= 3:
#         return n
#     if 3 < n <= 32:
#         return n // 4 + f(n - 3)
#     if n > 32:
#         return 2 * f(n - 5)
#
# print(f(100))


# def all_even(x):
#     while x>0:
#         if (x % 10) % 2 != 0:
#             return False
#         x //= 10
#     return True
#
# @functools.lru_cache(None)
# def f(n):
#     if n <= 18:
#         return n + 3
#     if n > 18 and n % 3 == 0:
#         return (n // 3) * f(n // 3) + n - 12
#     if n > 18 and n % 3 != 0:
#         return f(n - 1) + n * n + 5
#
# count = 0
# for n in range(1, 1001):
#     if all_even(f(n)):
#         count += 1
# print(count)

# def f(n):
#     if n > 30:
#         return n * n + 5 * n + 4
#     if n <= 30 and n % 2 == 0:
#         return f(n + 1) + 3 * f(n + 4)
#     if n <= 30 and n % 2 != 0:
#         return 2 * f(n + 2) + f(n + 5)
#
# n = 1
# count = 0
# while n < 1000:
#     if sum(map(int, str(f(n)))) == 27:
#         count += 1
#     n += 1
# print(n)
# print(count)


...
# n = 1
# count = 0
# while True:
#     try:
#         if 100 <= f(n) <= 999:
#             count += 1
#             print(count)
#     except:
#         pass
#     n += 1



# def f(n):
#     if n < 3: return n + 1
#     if n >= 3 and n % 2 == 0:
#         return f(n - 2) + n - 2
#     if n >= 3 and n % 2 != 0:
#         return f(n + 2) + n + 2
#
# n = 1
# count = 0
# while True:
#     try:
#         if 10000 <= f(n) <= 99999:
#             count += 1
#             print(count)
#     except:
#         pass
#     n+= 1


# def f(n):
#     if n == 1: return 1
#     if n %2 == 0:
#         return n + f(n - 1)
#     if n > 1 and n % 2 != 0:
#         return 2 * f(n - 2)
#
# print(f(26))








