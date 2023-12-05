# def f(x,y, a):
#     return (x + 2*y < a) or (y > x) or (x > 60)
# print(min(a for a in range(0, 1000) if all(f(x, y, a) for x in range(-100,100) for y in range(-100,100))))

# def f(x, y, a):
#     return (x*y < a) or (x < y) or (9 < x)
# print(min(a for a in range(0, 100) if all(f(x,y,a) for x in range(0,100) for y in range(0, 100))))

# def f(x,y, a):
#     return (x + 2*y != 58) or ((a - x > 0) == (a + y > 0))
# print(min(a for a in range(1, 100) if all(f(x,y, a) == 1 for x in range(1,200) for y in range(1,200))))

# def f(x, y, a):
#     return (x >= 9) or (2*x < y) or (x*y < a)
# print(min(a for a in range(0, 1000) if all(f(x,y, a) for x in range(0, 100) for y in range(0, 100))))

# def f(x, y, a):
#     return (x + y <= 32) or (y <= x + 4) or (y >= a)
# print(max(a for a in range(0, 100) if all(f(x, y, a) for x in range(0, 100) for y in range(0, 100))))

# def d(n, m):
#     return n % m == 0
# def f(x,a):
#     return (d(x, 13) <= (x not in range(40, 61))) or (a < x + 20)
# print(max(a for a in range(1, 200) if all(f(x,a) for x in range(1, 200))))



# def d(n, m):
#     return n % m == 0
# def f(x, a):
#     return (d(x, 2) <= (not d(x, 3)) or (x + a >= 100))
# print(min(a for a in range(1, 200) if all(f(x, a) for x in range(1, 200))))

# def p(n, m):
#     if (n - m) > 0: return True
#     else: return False
# def f(x, y, a):
#     return (not p(x + y, 73)) or (not p(37, x - y)) or p(y, a)
# print(max(a for a in range(0, 200) if all(f(x, y, a) for x in range(0, 100) for y in range(0, 100))))

# def d(n, m):
#     return n % m == 0
# def f(x, a):
#     return (d(x, 3) <= (not d(x, 2))) or (x - a >= 4)
# print(max(a for a in range(1, 300) if all(f(x, a) for x in range(1, 200))))

# def d(n, m):
#     return n % m == 0
# def s(s, d):
#     return s + d > 0
# def f(x, a):
#     return (x + a >= 160) or (d(x, 7) <= (not s(x, -17)))
# print(min(a for a in range(1, 1000) if all(f(x, a) for x in range(1, 200))))

# def f(x, a):
#     return (x&a != 0) <= (((x & 17 == 0) and (x & 5 == 0)) <= (x & 3 != 0))
# print(max(a for a in range(0, 300) if all(f(x, a) for x in range(0, 300))))

# def f(x, a):
#     return ((x & 103 == 0) and (x & 94 != 0)) <= (x & a != 0)
# print(min(a for a in range(1, 100) if all(f(x, a) for x in range(1, 200))))

# def f(x, a): return ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & a == 0))
# print(min(a for a in range(0, 100) if all(f(x, a) for x in range(0, 200))))

def f(x, a):
    return ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0))) <= ((x & 8 != 0) and (x & a != 0) and (x & 58 == 0))
print(min(a for a in range(1, 200) if all(f(x, a) == 0 for x in range(1, 200))))

