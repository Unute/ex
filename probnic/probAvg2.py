
# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = (w == z) or (x and not(y)) or w
#                 if f == 0:
#                     print(w,x,y,z)

#


# def f(N):
#     n = bin(N)[2:]
#     if int(n) % 11 == 0:
#         n += n.count('0') * '0'
#     else:
#         n = (n.count('1') * '1') + n
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) % 227 == 0:
#         print(N)
#         break
#     N += 1


# from turtle import *
#
# m = 40
# tracer(5)
#
# for i in range(16):
#     lt(36)
#     fd(4 * m)
#     lt(36)
#
# up()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x *m, y*m)
#         dot(4, 'blue')
# input()

# import itertools
#
# a = list(itertools.product('аимнр', repeat = 5))
#
# n = 1
# for x in a:
#     x = ''.join(x)
#     if x == 'наири':
#         break
#     n += 1
# print(n)

# x = 7*5**123 + 6*5**111 - 5*25**50 + 4*125**30 - 3*5**10
# n = 0
# while x > 0:
#     if x % 5 == 4:
#         n += 1
#     x //= 5
# print(n)

# def f(x, y, a):
    # return (2*x + 3*y == 101) and (x + y < a)

# print(max(a for a in range(-100, 100) if all(f(x, y, a) == 0 for x in range(1, 100) for y in range(1, 100))))

def f(s, c, m):
    if s >= 125: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s + 2, c + 1, m), f(s+4, c + 1, m), f(s*2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for s in range(1, 125):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 4:
                print(s, m)
            break

# print((600*2**13)/(640*480))
# print(2**5)



# 59