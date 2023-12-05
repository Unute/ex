# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = x or ((not y) or z or (not w)) and (y or (not z))
#                 if f == 0:
#                     print(x, y, z, w)

# def f(N):
#     n = bin(N)[2:]
#     n += n[-2]
#     n += n[1]
#     return int(n, 2)
#
# N = 2
# while True:
#     if f(N) > 100:
#         print(N)
#         break
#     N += 1


# from turtle import *
#
# m = 30
# tracer(10)
#
# up()
# goto(0, 10*m)
# down()
#
# rt(45)
# for i in range(7):
#     fd(6*m)
#     rt(45)
#     fd(12*m)
#     rt(135)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# input()

# import itertools
#
# a = list(itertools.product('гепард', repeat = 5))
#
# n = 0
# for x in a:
#     x = ''.join(x)
#     if x[0] != 'а' and x.count('г') == 1 and x[-1] != 'е':
#         n += 1
# print(n)

# for n in range(5, 100):
#     s = '1'+ '3' * n
#
#     while '12' in s or '233' in s or '3333' in s:
#         if '12' in s:
#             s = s.replace('12', '332', 1)
#         if '233' in s:
#             s = s.replace('233', '23', 1)
#         if '3333' in s:
#             s = s.replace('3333', '32', 1)
#
#     if sum(map(int, s)) % 6 == 0:
#         print(sum(map(int, s)), n)
#         break
# print(sum(map(int, s)), n)

# ip1 = [bin(int(x))[2:].zfill(8) for x in '193.175.175.231'.split('.')]
# ip2 = [bin(int(x))[2:].zfill(8) for x in '193.175.176.118'.split('.')]
# print(*ip1)
# print(*ip2)
# print(int('11110000', 2))

# for x in '0123456789abcde':
#     a = int('97968' + x + '15', 15) + int('7' + x + '233', 15)
#     if a % 14 == 0:
#         print(x, a // 14)

# def f(x, d, c, a):
#     for d in range(13, 58):
#         for c in range(29, 80):
#             return (x in d) <= (( (not(x in c)) and (not(x in a)))) <= (not(x in d))
#
# print(min(a for a in range(-500, 500) if all(f(x, d, c ,a) for x in range(-500, 500))))
#
# def f(x, d, a):
#     return (not(x in a)) <= (not(x in d))
#
# print(min(a for a in range(-100, 100) if all(f(x, d, a) for x in range(17, 29) for d in range(17, 59))))

import functools

# @functools.lru_cache(None)
# def f(n):
#     if n < 3: return 1
#     if n > 2 and n % 2 == 0:
#         return f(n-1) + n - 1
#     if n > 2 and n % 2 != 0:
#         return f(n-2) + 2*n - 2
#
# print(f(2048) - f(2045))
# print(f(29))


# def f(a, b, c, m):
#     if a + b >= 68: return c % 2 == m % 2
#     if c == m: return
#     h = [f(a + 1,b , c+ 1, m), f(a, b + 1, c + 1, m), f(a + b, b, c+ 1, m), f(a, b + a, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 59):
#     for m in range(1, 5):
#         if f(8, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

# import re
#
# for x in range(0, 10**8 + 1, 237):
#     if re.fullmatch('81.2.*80', str(x)) is not None and re.fullmatch('.*9.*', str(x)) is None:
#         print(x, x // 237)

# 67