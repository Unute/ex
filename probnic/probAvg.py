# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((x <= y) or (z <= w)) and (not(x <= w))
#                 if f == 1:
#                     print(x,y,z,w)

from turtle import *

# m = 18
# tracer(10)
#
# down()
# for i in range(10):
#     fd(10*m)
#     rt(90)
# up()
# fd(3* m)
# lt(90)
# fd(5*m)
# rt(90)
# down()
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(12*m)
#     rt(90)
#
#
# up()
# for x in range(-40, 40):
#     for y in range(-40,40):
#         goto(x * m, y * m)
#         dot(4, 'blue')
# input()

# def d(n, m):
#     return n % m ==0
#
# def f(a, x):
#     return d(x, a) <= (not d(x, 12))
#
# print(min(a for a in range(1, 100) if all(f(a, x)== 1 for x in range(30, 45))))

def f(s, c ,m):
    if s >= 419: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s + 1, c + 1, m), f(s + 3, c + 1, m), f(s * 5, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for s in range(1, 420):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 4:
                print(s, m)
            break

# 19  17
# 20
# 21


# 62