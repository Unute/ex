# def f(x, end):
#     if x > end or x == 11: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x * 2,end) + f(x ** 2, end)
#
# print(f(2, 20))

# def f(x, end):
#     if x > end or x == 17: return 0
#     if x == end: return 1
#     return f(x + 2, end) + f(x + 3, end) + f(x * 2, end)
# print(f(3, 10) * f(10, 25))

# def f(x, end):
#     if x > end or x == 16: return 0
#     if x == end: return 1
#     return f(x + 3, end) + f(x + 5, end) + f(x * 2, end)
# print(f(4, 32) * f(32, 68))
# 7524 + 8046

# def f(x, end):
#     if x < end or x == 7: return 0
#     if x == end: return 1
#     return f(x - 1, end) + f(x - 3, end) + f(x // 2, end)
# print(f(19, 10) * f(10, 3))

# def f(x, end):
#     if x > end or x == 90: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x * 2, end) + f(x * 3,end)
# print(f(3 , 30) * f(30, 100) * f(100, 184))

# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 3, end) + f(x * 2, end)
# print(f(3, 9) * f(9, 12) * f(12, 20))

# def f(x, a):
#     if x > a: return 0
#     if x == a: return 1
#     return f(x + 2, a) + f(x + 3, a) + f(int(str(x) + '1'), a)
# print(f(3, 12) * f(12, 25))

# def f(x, a):
#     if x > a or x == 12: return 0
#     if x == a: return 1
#     return f(x + 1, a) + f(x + 2, a) + f(x * 3, a)
# print(f(2, 9) * f(9, 19))

# def f(x , a):
#     if x < a: return 0
#     if x == a: return 1
#     return f(x - 1, a) + f(x // 2, a)
# print(f(30, 12) * f(12, 1))

# def f(x, a):
#     if x > a or x == 13: return 0
#     if x == a: return 1
#     return f(x + 1, a) + f(x + 2 , a) + f(x * 3, a)
# print(f(3 ,8) * f(8, 18))

# def f(x, a):
#     if x > a or x == 13: return 0
#     if x == a: return 1
#     return f(x + 2, a) + f(x + 3, a) + f(x + 5, a)
# print(f(5, 17) * f(17, 25))
# print(126 + 126)

# def f(x, a):
#     if x > a: return 0
#     if x == a: return 1
#     return f(x + 1, a) + f(x * 2, a)
# print(f(2, 7) * f(7,16) * f(16, 39))

# def f(x, a):
#     if x < a: return 0
#     if x == a: return 1
#     return f(x - 2, a) + f(x - 5, a)
# print(f(23, 2))

# def f(x, a):
#     if x > a: return 0
#     if x == a: return 1
#     return f(x + 1, a) + f(x + 3, a) + f(x * 3, a)
# print(f(4, 8))





