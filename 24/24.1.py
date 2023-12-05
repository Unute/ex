# a = open('24.txt').readline()
# count = 1
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] != a[i + 1]:
#         count += 1
#         m = max(m, count)
#     else:
#         count = 1
# print(m)

# from itertools import product as pd
#
# a = open('24.txt').readline()
# count = 1
# f = list(pd('XYZ', repeat= 2))
# m = -float('inf')
# for i in range(len(a) - 1):
#     if all(''.join(s) != (a[i] + a[i + 1]) for s in f):
#         count += 1
#         m = max(m, count)
#     else:
#         count = 1
# print(m)
#  другим способом
# s = 'xxabcdxxxabc'
# print(s.replace('xx', 'x x').replace('xx', 'x x'))
# a = open('24.txt').readline()
# a = a.replace('Y', 'X').replace('Z', 'X').replace('XX', 'X X').replace('XX', 'X X')
# print(max(len(s) for s in a.split()))

# a = open('24.txt').readline()
# a = a.replace('ab', 'a d').replace('da', 'd a')
# print(max(len(s) for s in a.split()))

# a = open('24.txt').readline()
# a = a.replace('PR', 'P R').replace('RP', 'R P')
# print(max(len(s) for s in a.split()))
# count = 1
# m = -float('inf')
# for i in range(len(a) - 1):
#     if (a[i] + a[i + 1]) != 'PR' and (a[i] + a[i + 1]) != 'RP':
#         count += 1
#         m = max(m, count)
#     else:
#         count = 1
# print(m)

# a = open('24.txt').readline()
# a = a.replace('QW', 'Q W')
# print(max(len(s) for s in a.split()))

# a = open('24.txt').readline()
# a = a.replace('PP', 'P P').replace('PP', 'P P')
# print(max(len(s) for s in a.split()))
# count = 1
# m = -float('inf')
# for i in range(len(a) - 1):
#     if (a[i] + a[i + 1]) != 'PP':
#         count += 1
#         m = max(m, count)
#     else:
#         count = 1
# print(m)

# a = open('24.txt').readline()
# count = 1
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] != a[i + 1]:
#         count += 1
#         m = max(m, count)
#     else:
#         count = 1
# print(m)

# a = open('24.txt').readline()
# count = 1
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] == a[i + 1]:
#         count += 1
#         m = max(m, count)
#     else:
#         count = 1
# print(m)