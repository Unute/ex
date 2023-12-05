# from itertools import product as pd
# from itertools import permutations as pr
#
# def f(x,y,w,z):
#     return (w != y) and (z <= w) and (not x)
# for x1,x2,x3,x4,x5,x6 in pd([0,1], repeat = 6):
#     t = (
#         (x1,x2,x3,1,1),
#         (1,x4,1,x5,1),
#         (0,x6,1,0,1)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r= 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)

# def f(N):
#     n = bin(N)[2:]
#     if n.count('1') % 2 == 0:
#         n += '0'
#     if n.count('1') % 2 != 0:
#         n += '1'
#     if n.count('1') % 2 == 0:
#         n += '0'
#     if n.count('1') % 2 != 0:
#         n += '1'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) > 96:
#         print(f(N))
#         break
#     N += 1

# from turtle import *
#
# tracer(10)
# m = 8
# up()
# goto(20*m, 35*m)
# down()
#
# for i in range(100):
#     fd(10 * m)
#     rt(8)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*m, y*m)
# input()

# import itertools
# a = list(itertools.product('123456789', repeat = 6))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x[0] != '5' and x.count('2') == 2:
#         count += 1
# print(count)

# n = 0
# for line in open('9prob.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     a.sort()
#     if len(p) >= 2:
#         print(a)



# s = '3' * 30 + '4' * 30 + '5' * 30
# while '43' in s or '53' in s:
#     if '43' in s:
#         s = s.replace('43','33', 1)
#     else:
#         s = s.replace('53', '433', 1)
# print(s)

# k=0
# x = 3*16**2018 - 2*8**1028 - 3*4**1100 - 2**1050 - 2022
# while x > 0:
#     if x % 4 == 3:
#         k += 1
#     x//=4
# print(k)

# p = [i / 10 for i in range(5*10, 30*10)]
# q = [i / 10 for i in range(14*10, 23 * 10)]
#
# def f(x, a):
#     return ((x in p) == (x in q)) <= (x not in a)
#
# a = set([i/10 for i in range(1*10, 35*10)])
# for x in [i/10 for i in range(1*10, 35*10)]:
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))

# def f(s,c,m):
#     if s >= 22: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 22):
#     for m in range(1,10):
#         if f(s, 0, m):
#             if m == 8:
#                 print(s, m)
#             break

# def f(x, a):
#     if x > a or x == 14: return 0
#     if x == a: return 1
#     return f(x + 1, a) + f(x + 3, a)
# print(f(2, 9) * f(9,18))

# ip1 = [bin(int(x))[2:].zfill(8) for x in '133.57.64.130'.split('.')]
# ip2 = [bin(int(x))[2:].zfill(8) for x in '133.57.64.0'.split('.')]
# print(*ip1)
# print(*ip2)

# 51