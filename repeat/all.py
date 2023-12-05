# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             f = ((not x) and y and z) or ((not x) and (not z))
#             if f == 1:
#                 print(x,y,z)
import itertools

# def f(N):
#     n = bin(N)[2:]
#     if n.count('0') == n.count('1'):
#         n += n[-1]
#     else:
#         if n.count('0') < n.count('1'):
#             n += '0'
#         if n.count('0') > n.count('1'):
#             n += '1'
#     if n.count('0') == n.count('1'):
#         n += n[-1]
#     else:
#         if n.count('0') < n.count('1'):
#             n += '0'
#         if n.count('0') > n.count('1'):
#             n += '1'
#     if n.count('0') == n.count('1'):
#         n += n[-1]
#     else:
#         if n.count('0') < n.count('1'):
#             n += '0'
#         if n.count('0') > n.count('1'):
#             n += '1'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) % 4 == 0 and f(N) % 8 != 0:
#         print(N)
#     N += 1



# from turtle import *
# m = 5
# tracer(10)

# for i in range(8):
#     goto(30*m, 10*m)
#     goto(50*m, -30*m)
#     goto(-40*m, 50*m)
# up()
# for x in range(-50,50):
#     for y in range(-50, 50):
#         goto(x*m, y*m)
#          dot(3, 'blue')
# input()

# import itertools
#
# a = list(itertools.product('01234567', repeat = 4))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x[0] != '0' and int(x) % 4 == 0:
#         count += 1
#         print(x)
# print(count)

# x = 5*343**8 + 4*49**12 + 7**14 - 98
# a1 = 0
# while x > 0:
#     if x % 7 == 0:
#         a1 += 1
#     x //= 7
# print(a1)

# def f(x, a, p ,q):
#     ((x in a) <= (x in p)) or (x in q)
#
# print(max(a for a in range(-100, 100) if all(f(x, a, p ,q) for x in range(-100, 100) for p in range(43,49) for q in range(44,53))))

# def f(n):
#     if n < 0: return -n
#     if n % 2 == 0:
#         return 2 * n + 1 + f(n - 3)
#     if n % 2 != 0:
#         return 4 * n + 2 * f(n-4)
#
# print(f(33))


# def f(s, c, m):
#     if s > 33: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m), f(s + 3, c + 1, m), f(s*2 ,c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 33):
#     for m in range(1, 5):
#         if f(s, 0 ,m):
#             if m == 4:
#                 print(s, m)
#             break

# a = list(itertools.product('агмнсту', repeat = 6))
# n = 0
# for x in a:
#     x = ''.join(x)
#     n += 1
#
#     if x[0] != 'у' and x.count('м') == 2 and x.count('г') <= 1:
#         print(x, n)
# print(n)

# import threading
# import sys
# import functools
#
# threading.stack_size(4096 * 4096 * 8)
# sys.setrecursionlimit(9999)
# @functools.lru_cache(None)
# def f(n):
#     if n < 11: return n
#     if n >= 11:
#         return n + f(n - 1)
#
# print(f(2024) - f(2021))
#
# new_thread = threading.Thread(target=thr, args=[])
# new_thread.start()
















# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (z <= w) and y and (not x)
#                 if f == 1:
#                     print(x,y,z,w)

# def f(N):
#     n = bin(N)[2:]
#     n += n[-1]
#     if n.count('1') % 2 == 0:
#         n += '0'
#     else:
#         n += '1'
#     if n.count('1') % 2 == 0:
#         n += '0'
#     else:
#         n += '1'
#     return int(n, 2)
# N = 1
# while True:
#     if f(N) > 114:
#         print(f(N))
#         break
#     N += 1


# from turtle import *
#
# m = 15
# tracer(10)
# up()
# goto(0, 10 *m)
# down()
#
# for i in range(13):
#     fd(10*m)
#     rt(90)
#     fd(10*m)
#     rt(90)
#     fd(30*m)
#     rt(90)
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y * m)
#         dot(4, 'blue')
# input()

import itertools

# x = 8**2014 - 2**614 + 45
# a = bin(x)[2:]
# print(a.count('1'))


# def f(x):
#     return (a % 35 == 0) and ((730 % x == 0) <= ((a % x != 0) <= (110 % x != 0)))
# count = 0
# for a in range(1, 1001):
#     if all(f(x) for x in range(1, 10000)):
#         count += 1
# print(count)

# import math
#
# count = 0
# def f(n):
#     try:
#         if n == 0: return 0
#         if n > 0 and n % 10 == 0:
#             return f(n // 10)
#         if n > 0 and n % 10 > 0 and math.floor(math.log(n, 10)) % 2 == 0:
#             return f(n - 1) - 1
#         if n > 0 and n % 10 > 0 and math.floor(math.log(n, 10)) % 2 != 0:
#             return f(n - 1) + 1
#     except:
#         ...

# n = 0
# while n <= 10**6:
#     if f(n) == 0:
#         count += 1
#     n += 1
# print(count)

# ip1 = [bin(int(x))[2:].zfill(8) for x in '211.115.61.154'.split('.')]
# ip2 = [bin(int(x))[2:].zfill(8) for x in '211.115.59.137'.split('.')]
# print(*ip1)
# print(*ip2)
# print(int('11111000', 2))



# def f(N):
#     n = bin(N)[2:]
#     if N % 3 == 0:
#         n += n[-3:]
#     if N % 3 != 0:
#         ost = (N % 3) * 3
#         n += bin(ost)[2:]
#     return int(n, 2)

# N= 4
# while True:
#     if f(N) == 163:
#         print(f(N))
#     N += 1

# import itertools
# k = 0
# n = [''.join(i) for i in itertools.product('0246', repeat = 2)] + [''.join(i) for i in itertools.product('1357', repeat = 2)]
# for x in itertools.permutations('01234567', r=5):
#     s = ''.join(x)
#     if all(i not in s for i in n) and x[0] != '0' and x.count('1') == 0:
#         k += 1
# print(k)

# k = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 4 and len(np) == 3:
#         if (sum(p) / len(p)) < (sum(a) / len(a)):
#             k += 1
# print(k)


# for n in range(1, 10001):
#     s = '5' + '2' * n
#     while '52' in s or '2222' in s or '1122' in s:
#         s = s.replace('52', '11', 1)
#         s = s.replace('2222', '5', 1)
#         s = s.replace('1122', '25', 1)
#     if sum(map(int, s)) == 64:
#         print(n)


# x = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 -2024
# k = 0
# while x > 0:
#     if x % 25 == 0:
#         k += 1
#     x //= 25
# print(k)

# def f(x, y, a):
#     return (x + 2*y < a) or (y > x) or (x > 60)
# print(min(a for a in range(0, 1000) if all(f(x, y, a) for x in range(0, 150) for y in range(0, 150))))

# def f(n):
#     if n > 2024:
#         return n
#     if n <= 2024:
#         return n * f(n + 1)
# print(f(2022) / f(2024))

# def f(s, c, m):
#     if s > 129: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 129):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break
# 64
# 32 63
# 62

# def f(x, a):
#     if x > a or x == 11: return 0
#     if x == a: return 1
#     return f(x + 1, a) + f(x * 2, a) + f(x ** 2, a)
#
# print(f(2, 20))

# def f(x, a):
#     if x > a or x == 16: return 0
#     if x == a: return 1
#     return f(x + 3, a) + f(x + 5, a) + f(x * 2, a)
# print(f(4, 32) * f(32, 68))
# print(7524 + 8046)


# from itertools import product as pd
# from itertools import permutations as pr
#
# def f(x,y,w,z):
#     return (not (y <= x)) or (z <= w) or (not z)
#
# for x1,x2,x3,x4,x5,x6,x7 in pd([0,1], repeat = 7):
#     t = (
#         (x1,0,x2,x3,0),
#         (0,1,x4,x5,0),
#         (1,x6,x7,0,0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r= 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)

# k = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if a[0] == 1 and (a[1] >= 85 or a[2] >= 85):
#         k += 1
# print(k)

# n = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     if (a[0] == 1 or a[0] == 3 or a[0] == 5) and (a[1] < 36 and a[2] < 43):
#         print(a)
#         n += 1
# print(n)

# n = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     if a[1] >= 37 and a[2] <= 43:
#         n += 1
# print(n)

# n =  0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     if a[1] > a[2] and a[2] >= 44:
#         n += 1
# print(n)


# count = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     nch = [x for x in a if x % 2 != 0]
#     ch = [x for x in a if x % 2 == 0]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 2]
#     if (sum(nch) > sum(ch)) != (len(p) == 2):
#         count += 1
# print(count)


# a = [int(x) for x in open('17rep.txt')]
# count = 0
# m = float('inf')
# mx = max(x for x in a if x % 111 == 0)
# for i in range(len(a) - 1):
#     if (a[i] > mx) or (a[i + 1] > mx):
#         if a[i] % 10 == 7 or a[i + 1] % 10 == 7:
#             count += 1
#             m = min(m, a[i] + a[i + 1])
# print(count, m)

# from itertools import product as pd
# from itertools import permutations as pr
#
# def f(x,y,w,z):
#     return (((not y) <= w) <= (x <= z)) <= (x <= w)
#
# for x1,x2,x3,x4,x5,x6 in pd([0,1], repeat = 6):
#     t = (
#         (0,0,0,x1,0),
#         (0,0,x2,x3,0),
#         (0,x4,x5,x6,0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r= 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)

# import itertools
#
# a= list(itertools.permutations('0123456789', r = 6))
# b = list(itertools.permutations('02468', r = 2))
# c = list(itertools.permutations('13579', r = 2))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if all(b not in x) and all(c not in x):
#         count += 1
# print(count)



# from itertools import product as pd
# from itertools import permutations as pr
#
# def f(x, y,z,w):
#     return (x and (not y)) or (y == z) or (not w)
#
# for x1,x2,x3,x4 in pd([0,1], repeat = 4):
#     t = (
#         (0,x1,x2,0,0),
#         (0,1,0,1,0),
#         (x3,1,0,x4,0)
#     )
#     if len(t) == len(set(t)):
#         for p in pr('xywz', r= 4):
#             if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#                 print(*p)

# def f(N):
#     n = bin(N)[2:]
#     if n[::-1][0] == '0':
#         n = n[::-1]
#         n = n.replace('0', '', 1)
#     return int(n, 2)
# N = 1
# while True:
#     if N > 100:
#         if f(N) == 7:
#             print(N)
#     N += 1
# print()

import itertools
import re

# a = list(itertools.product('0123456789', repeat = 6))
#
# count = 0
# for x in a:
#     x = ''.join(x)
#     x1 = x[0] + x[1] + x[2]
#     x2 = x[-1] + x[-2] + x[-3]
#     if sum(map(int, x1)) == sum(map(int, x2)) and x1!=x2:
#         for i in range(len(x2)):
#             for j in range(len(x1)):
#                 if x1[j] == x2[i]:
#                     count += 1
# print(count)


# count = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     if a[0] + a[1] + a[2] > 180:
#         count += 1
# print(count)

# p = [1,3,5,7,9,11]
# q = [3,6,9,12]
#
# def f(x, a):
#     return ((x in p) <= (x not in q)) or (x in a)
#
# a = set()
# for x in range(20):
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))

# a = [int(x) for x in open('17rep.txt')]
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     if (a[i] * a[i + 1]) > (a[i] + a[i + 1]):
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)

# def f(a, b, c, m):
#     if a + b >= 79: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a + b, b, c+ 1, m), f(a, b + a, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
# for s in range(1, 70):
#     for m in range(1, 6):
#         if f(9, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

# def f(x, a):
#     if x > a or x == 30: return 0
#     if x == a: return 1
#     return f(x + 1, a) + f(x * 3, a) + f(x *4, a)
# print(f(2,15) * f(15,100))


#51

# import re
#
# for x in range(0, 10**8+ 1, 2025):
#     if re.fullmatch('12.*34.5', str(x)) is not None:
#         if x % 2025 == 0:
#             print(x, x // 2025, end='')


# import re
# for x in range(0, 10**8 + 1, 1923):
#     if re.fullmatch('1.*2..76', str(x)) is not None:
#         print(x, x // 1923, end = ' ')

# for x in range(500001, 500100):
#     D = set()
#     for d in range(2, int(x ** 0.5 + 1)):
#         if x % d == 0:
#             if d % 10 == 8 and d != 8:
#                 D.add(d)
#             if (x // d) % 10 == 8 and (x // d) != 8:
#                 D.add(x // d)
#     if len(D) >= 1:
#         print(x, min(D))

# from fnmatch import fnmatch
# import re
# for x in range(500001, 1000100):
#     if re.fullmatch('123.*4.5', str(x)) is not None:
#         D = set()
#         for d in range(1, int(x ** 0.5) + 1):
#             if x % d == 0:
#                 D.add(d)
#                 D.add(x // d)
#         if fnmatch(str(sum(D)), '*7?'):
#             print(x, sum(D))



# import re
# for x in range(65001, 700000):
#     if re.fullmatch('6.*97.*5.', str(x)):
#         D = set()
#         for d in range(1, int(x ** 0.5) + 1):
#             if x % d == 0:
#                 if d % 2 == 0: D.add(d)
#                 if (x // d) % 2 == 0: D.add(x // d)
#         if len(D) >= 4:
#             print(x, sum(D))

# import re
# for x in range(0, 10 ** 8 + 1, 253):
#     if re.fullmatch('12..15.*6', str(x)) is not None:
#         if x % 253 == 0:
#             print(x, x // 253, end = ' ')


# import re
# for x in range(0, 10 ** 8 + 1, 237):
#     if re.fullmatch('81.2.*80', str(x)) is not None:
#         if re.fullmatch('.*9.*', str(x)) is None:
#             print(x, x // 237, end = ' ')

# import re
# for x in range(0, 10**8 + 1, 161):
#     if re.fullmatch('12.*4.65', str(x)) is not None:
#         if x % 161 == 0:
#             print(x, x // 161, end = ' ')

# import re
# for x in range(0, 10 ** 8 + 1, 141):
#     if re.fullmatch('1234.*7', str(x)) is not None:
#         if x % 141 == 0:
#             print(x, x // 141, end = ' ')

# import re
# for x in range(0, 10**8 + 1, 27):
#     if re.fullmatch('123.*890', str(x)) is not None:
#         if x % 27 == 0:
#             print(x, x // 27, end = ' ')

# import re
# for x in range(0, 10**9 + 1, 151):
#     if re.fullmatch('2.34.56.8', str(x)) is not None:
#         if x % 151 == 0:
#             print(x, x // 151, end = ' ')


# import re
# for x in range(0, 10** 6 + 1):
#     if re.fullmatch('4.*', str(x)) is not None:
#         D = set()
#         for d in range(1, int(d ** 0.5) + 1):
#             if x % d == 0:
#                 D.add(d)
#                 D.add(x // d)
#         if len(D) == 24:
#             if re.fullmatch('4.*', str(max(D)) is not None:
#                 print(x, max(D))
# print(D)

# count = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if ((a[0] + a[-1]) ** 2) > (a[1]**2 + a[2] ** 2 + a[3] ** 2):
#         count += 1
# print(count )

# from fnmatch import fnmatch
# for x in range(0, 10**10, 73):
#     if fnmatch(str(x), '12345*76'):
#         print(x)


# k = 0
# count = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     p1 = [x for x in a if a.count(x) == 3]
#     a.sort()
#     if sum(a) == 180:
#         k += 1
#     if (len(p) == 2 or len(p1) == 3) and sum(a) == 180:
#         count += 1
# print((count / k) * 100)

# from fnmatch import fnmatch
#
# for x in range(0, 10 ** 8 + 1, 237):
#     if fnmatch(str(x), '81?2*80') and not fnmatch(str(x), '*9*'):
#         print(x, x // 237)

# def f(x, a):
#     if x < a: return 0
#     if x == a: return 1
#     return f(x - 2, a) + f(x // 3, a)
# print(f(200, 6) * f(6, 2))




