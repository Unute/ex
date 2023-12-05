
# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 4 and len(np) == 3:
#         if (sum(p) / len(p)) < (sum(a) / 7):
#             count += 1
# print(count)


# p = [3,6,9,12]
# r = [1,2,3,4,5,6]
#
# def f(x, a):
#     return not((x not in a) and (x in p)) or (x not in r)
# a = set()
# for x in range(0, 15):
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))

# def f(n):
#     if n <= 3: return n
#     if n > 3 and n % 3 == 0: return n**3 + f(n - 1)
#     if n > 3 and n % 3 == 1: return  4 + f(n//3)
#     if n > 3 and n % 3 == 2: return n**2 + f(n - 2)
# print(f(100))


# def s5(x):
#     s = ''
#     while x > 0:
#         s += str(x % 5)
#         x //= 5
#     return s[::-1]

# def s3(x):
#     s = ''
#     while x > 0:
#         s += str(x % 3)
#         x //= 3
#     return s[::-1]
# count = 0
# x = 0
# while True:
#     if len(s5(x)) == 4 and len(s3(x)) == 5 and hex(x)[2:][-1] == 'd':
#         print(x)
#     x += 1
# print(count)

# for x in range(0, 20):
#     if hex(x)[2:] == 'd':
#         print(x)

# count = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     if a[1] > a[2] and a[2] >= 44:
#         count += 1
# print(count)

# count = 0
# for line in open('9rep.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if ((a[0] + a[2]) / 2) == a[1]:
#         count += 1
# print(count)







