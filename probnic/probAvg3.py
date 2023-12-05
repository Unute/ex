# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = w and ((x <= y) == (y <= z))
#                 if F == 1:
#                     print(x,y,z,w)

# def d(x):
#     s = ''
#     while x > 0:
#         s += str(x % 4)
#         x //= 4
#     return s[::-1]
#
#
# def f(N):
#     n = d(N)
#     if int(n) % 3 == 0:
#         n = '2' + n + '11'
#     else:
#         n = '13' + n + '02'
#     R = int(n, 4)
#     return R
#
# N = 1
# while True:
#     if f(N) >= 1000:
#         print(f(N))
#         break
#     N += 1

# from turtle import *
#
# m = 25
# tracer(10)
#
# down()
# for i in range(5):
#     goto(5 * m, 4 * m)
#     goto(4 * m, -4 * m)
#     goto(-7 * m, -2 * m)
#     goto(-2 * m, 2 * m)
#
# up()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# input()

import itertools

a = list(itertools.product('руслан', repeat = 5))

count = 0
for x in a:
    x = ''.join(x)
    if x.count('р') == 1 or x.count('с') == 1 or x.count('л') == 1 or x.count('н') == 1:
        count += 1
        print(x)
print(count)

# for m in range(1000):
#     s = '4' + '6' * m
#     while '46' in s or '666' in s:
#         if '46' in s:
#             s = s.replace('46', '5', 1)
#         if '666' in s:
#             s = s.replace('666', '4', 1)
#     print(sum(map(int, s)), m)

# for x in '0123456789abcdefghijk':
#     c = int('18' + x + '89957', 22) + int('80' + x + '33', 22) + int('521' + x + '6', 22)
#     if c % 21 == 0:
#         print(c, x, c // 21)

# def d(n, m):
#     return n % m == 0
#
# def f(x, a):
#     return (d(x, 2) <= (not d(x,3))) or (x + a >= 100)
# print(min(a for a in range(1, 100) if all(f(x,a) == 1 for x in range(1, 100))))

# def f(s, c ,m):
#     if s >= 57: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m), f(s * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 57):
#     for m in range(1,5):
#         if f(s, 0, m):
#             if m == 2:
#                 print(s, m)
#             break