# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = (x and (not y)) or (y == z) or (not w)
#                 if f == 0:
#                     print(w, x, y, z)

def f(N):
    n = bin(N)[2:]
    if N % 3 == 0:
        n += n[-3:]
    else:
        ost = (N % 3) * 3
        n += bin(ost)[2:]
    R = int(n, 2)
    return R

N = 1
while True:
    if f(N) > 151:
        print(N)
        break
    N += 1
print(f(20))


# from turtle import *
#
# tracer(10)
# m = 25
# up()
# goto(-5 *m, 0)
# down()
#
# for i in range(7):
#     fd(10 * m)
#     rt(120)
#
# up()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# input()

# import itertools
#
# a = list(itertools.permutations('01234567', r = 5))
#
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x[0] != '0' and x.count('1') == 0 and x.count('02') == 0 and x.count('04') == 0 and x.count('06') == 0 and x.count('00') == 0 and x.count('20') == 0 and x.count('22') == 0 and x.count('24') == 0and x.count('26') == 0 and x.count('60') == 0 and x.count('62') == 0 and x.count('64') == 0 and x.count('66') == 0 and x.count('33') == 0 and x.count('35') == 0 and x.count('37') == 0 and x.count('53') == 0 and x.count('55') == 0 and x.count('57') == 0 and x.count('73') == 0 and x.count('75') == 0 and x.count('77') == 0 and x.count('40') == 0 and x.count('42') == 0 and x.count('44') == 0 and x.count('46') == 0:
#         count += 1
#         print(x)
# print(count)

# a = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
# for x in '0123456789ABCDEFGHI':
#     a = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
#     if a % 18 == 0:
#         print(x)
#         print(a // 18)
# print(16 // 18)

def f(x, y ,a):
    return (x + 2 * y < a) or (y > x) or (x > 60)
print(min(a for a in range(500) if all(f(x, y ,a) for x in range(100) for y in range(100))))

# def f(s, c, m):
#     if s >= 129: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 128):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break


# 67