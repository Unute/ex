from itertools import product as pd
from itertools import permutations as pr

# def f(w, x, y, z):
#     return (x and (not y)) or (x == z) or w
#
# for x1,x2,x3,x4 in pd([0,1], repeat = 4):
#     t = (
#         (1, x1, 0, 0, 0),
#         (1, 1, x2, 0, 0),
#         (x3, 1, 1, x4, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('wxyz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print


# def t(x):
#     s = ''
#     while x > 0:
#         s += str(x % 3)
#         x //= 3
#     return s[::-1]
#
# def f(N):
#     n = t(N)
#     if N % 2 == 0:
#         n = '1' + n + '00'
#     if N % 2 != 0:
#         n += t(sum(map(int, n)))
#     return int(n, 3)
# print(f(7))
#
# N = 0
# while True:
#     if f(N) > 168:
#         print(N)
#         break
#     N += 1
# print(f(1))

# from turtle import *
#
# m = 35
# tracer(10)
#
# for i in range(2):
#     fd(8 * m)
#     rt(90)
#     fd(10 * m)
#     rt(90)
# up()
# for i in range(3):
#     rt(90)
#     fd(7 * m)
#     rt(90)
# down()
# for i in range(2):
#     fd(-12 * m)
#     rt(90)
#     fd(13 * m)
#     rt(90)
# up()
# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# input()


# a = list(pd('01234567', repeat = 5))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x.count('3') == 1 and '35' not in x and '53' not in x and '36' not in x and '63' not in x and '73' not in x and '37' not in x and '38' not in x and '83' not in x:
#         print(x)
#         count += 1
# print(count)

# count = 0
# for line in open('9prob.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     count +=1
#     if len(p) == 2 and ((sum(p) / 2) >= (sum(np) // 4)):
#         print(a, p, np, (sum(p) / 4))
#         print(count)

# s = '>' + '1' * 26 + '2' * 10 + '3' * 14
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>', 1)
# s = s.replace('>', '')
# print(sum(map(int, s)))

# def f(x, a):
#     return ((x & 52 != 0) and (x & 36 == 0)) <= (x & a != 0)
# print(min(a for a in range(0, 200) if all(f(x, a) for x in range(0, 100))))

# def f(n):
#     if n < 10: return n
#     if n >= 10: return n % 10 + 8*f(n // 10)
# print(f(10**30))

# def f(x, y, c, m):
#     if x + y >= 16: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(x + 3, y, c + 1, m), f(x, y + 3, c + 1, m), f(x, y + 4, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 13):
#     for m in range(1, 5):
#         if f(s, 2, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

# def f(x, a):
#     if x > a: return 0
#     if x == a: return 1
#     return f(x +1, a) + f(x + 3, a) + f(x * 3, a)
# print(f(3, 9) * f(9, 27) * f(27, 31))

from fnmatch import fnmatch

# for x in range(600000, 1000000):
#     D = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             if d % 10 == 9 and d != 9 and d != x:
#                 D.add(d)
#             if (x // d) % 10 == 9 and (x // d) != 9 and (x // d) != x:
#                 D.add(x // d)
#     if len(D) >= 1:
#         print(x, min(D))

# a = [int(x) for x in open('17prob.txt')]
# count = 0
# m = float('inf')
# mx = max(x for x in a if str(x)[0] == '8')
# for i in range(len(a) - 2):
#     if ((abs(a[i]) // 100 == 6) + (abs(a[i + 1]) // 100 == 6) + (abs(a[i + 2]) // 100 == 6)) <= 1:
#         if (a[i] + a[i + 1] + a[i + 2]) >= mx:
#             count += 1
#             m = min(m, a[i] + a[i + 1] + a[i + 2])
# print(count, m)

# ip1 = [bin(int(x))[2:].zfill(8) for x in '111.81.27.224'.split('.')]
# ip2 = [bin(int(x))[2:].zfill(8) for x in '111.81.27.192'.split('.')]
# print(*ip1)
# print()
# print(*ip2)
# print(int('11000000', 2))

# s = 4*625**1920 + 4*125**x-4*25**1940 - 3*5**1950 - 1960
# def f(s):
#     g = ''
#     while s > 0:
#         g += str(s % 5)
#         s //= 5
#     return g
#
# for x in range(1, 100):
#     s = 4 * 625 ** 1920 + 4 * 125 ** x - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
#     s = f(s)
#     if s.count('0') == 1891:
#         print(x)
