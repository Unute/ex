# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = (x and (not y)) or (y == z) or (not w)
#                 if f == 0:
#                     print(w, x, y, z)

# from itertools import product as pd
# from itertools import permutations as pr
#
# def f(x, y, w, z):
#     return (x and (not y)) or (y == z) or (not w)
#
# for x1, x2, x3, x4 in pd([0, 1,], repeat = 4):
#     t = (
#         (x1, x2, 0, 0, 0),
#         (1, 0, x3, 0, 0),
#         (1, 0, 1, x4, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r=4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)

# from itertools import product as pd
# from itertools import permutations as pr
#
# def f(x, y, w, z):
#     return (y <= x) and (not z) and w
#
# for x1, x2, x3, x4, x5, x6 in pd([0, 1], repeat = 6):
#     t = (
#         (1, 0, x1, x2, 1),
#         (1, 1, x3, x4, 1),
#         (x5, 1, 1, x6, 1)
#     )
#
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r=4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)


from itertools import product as pd
from itertools import permutations as pr

# def f(x, y, w, z):
#     return (x and (not y)) or (x == z) or w
#
# for x1, x2, x3, x4 in pd([0, 1], repeat = 4):
#     t = (
#         (x1, x2, 0, 1, 0),
#         (1, 0, x3, 1, 0),
#         (1, 1, 0, x4, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r = 4):
#             if all(f(**dict(zip(p ,l))) == l[-1] for l in t):
#                 print(*p)


# def f(x, y, w, z):
#     return ((x or y) == (y <= z)) or w
#
# for x1, x2, x3, x4 ,x5, x6, x7, x8 in pd([0, 1], repeat = 8):
#     t = (
#         (x1, 1, x2, x3, 0),
#         (x4, x5, x6, 1, 0),
#         (1, x7, x8, 1, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r=4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)


# def f(x, y, w, z):
#     return ((not x) or y or (not z) or w) and (not((not x) or w))
#
# for x1,x2,x3,x4,x5 in pd([0, 1], repeat = 5):
#     t = (
#         (x1, 0, x2, 1, 1),
#         (0, x3, 0, x4, 1),
#         (1, 0, 0, x5, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)


# def f(a, b, c, t):
#     return ((not a) or (not b)) and (c <= (not a)) and ((t and (not a)) or (c and (not b)))
#
# t = (
#     (1,0,0,1,0),
#     (1,1,0,1,1),
#     (0,0,0,1,0),
#     (1,0,0,0,1)
# )
# for p in pr('abct' , r= 4):
#     if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#         print(*p)


# def f(x, y, w, z):
#     return ((w <= y) <= (x == y)) or (not z)
#
# for x1,x2,x3,x4,x5 in pd([0, 1], repeat = 5):
#     t = (
#         (x1, 0, 1, 0, 0),
#         (0, x2, x3, 0, 0),
#         (x4, 1, 1, x5, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)



# def f(x,y,w,z):
#     return ((x == z) or (x != w)) and ((y <= z) or (not z))
#
# for x1,x2,x3,x4,x5,x6,x7,x8,x9 in pd([0, 1], repeat = 9):
#     t = (
#         (1,x1,1,1,0),
#         (x2,1,x3,1,0),
#         (x4,1,1,1,0),
#         (1,x5,1,x6,0),
#         (x7,1,x8,x9,0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)



def f(x,y,w,z):
    return ((x <= z) and y) <= w

for x1,x2,x3,x4,x5,x6 in pd([0, 1], repeat = 6):
    t = (
        (0,0,0,x1,0),
        (0,0,x2,x3,0),
        (0,x4,x5,x6,0)
    )
    if len(t) == len(set(t)):
        for p in pr('xywz', r= 4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)



