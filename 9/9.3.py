# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) >= 2]
#     if a.count(min(a)) == 1 and len(p) >= 1:
#         if(max(a) + min(a)) < sum(p):
#             count += 1
#
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 3]
#     np = [x for x in a if a.count(x) == 1]
#     if (len(p) == 3 and len(np) == 4):
#         if (sum(np) / len(np)) <= (sum(p) / len(p)):
#             count += 1
# print(count)


count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     a.sort()
#     if len(p) == 2 and (a[-1] + a[-2]) > 2*(a[0] + a[1]):
#         if max(a) % min(a) != 0:
#             count += 1
# print(count)
# k = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     k += 1
#     if len(p) == 4 and len(np) == 3:
#         if a.count(max(a)) == 1:
#             print(k, a)
# print(42 + 48 + 38 + 57 + 17 + 42 + 17)

# k = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     k += 1
#     if len(p) == 2 and len(np) == 4:
#         if (sum(p) / len(p)) >= (sum(np) / len(np)):
#             print(k, a)

# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     p1 = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 2 and len(p1) == 2:
#         if (sum(p) / len(p)) <= int(np) <= (sum(p1) / len(p1)):
#             print(a)

# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     nch = [x for x in a if x % 2 != 0]
#     ch = [x for x in a if x % 2 == 0]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if (sum(nch) > sum(ch)) + (len(p) == 2 and len(np) == 3) == 1:
#         print(sum(nch),nch, sum(ch), p, np)
#         count += 1
# print(count)

# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     tri = [x for x in a if abs(x) % 10 == 3]
#     polog = [x for x in a if x > 0]
#     otr = [x for x in a if x < 0]
#     a.sort()
#     if len(tri) == 3 and ((sum(polog) ** 2) < (sum(otr) ** 2)):
#         count += 1
# print(count)

# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if (len(a) == len(set(a))) + (((a[-1] + a[0]) * 2) < (a[1] + a[2] + a[3])) == 1:
#         count += 1
# print(count)

# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if len(a) == len(set(a)):
#         if a[2] * 2 > a[-1] and a[2] * 2 > a[0] * 3:
#             count += 1
# print(count)