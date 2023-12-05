# a = []
# for line in open('9.txt'):
#     a.append([int(x) for x in line.split()])
#
# count = 0
# for line in a:
#     np = []
#     p = []
#     for x in line:
#         if line.count(x) == 2:
#             p.append(x)
#         if line.count(x) == 1:
#             np.append(x)
#     if len(p) == 4 and len(np) == 3:
#         if sum(line) / 7 > sum(p) / 4:
#             count += 1
# print(count)



# основная волна
# a = []
# for line in open('9.txt'):
#     a.append([int(x) for x in line.split()])
#
# for line in a:
#     np = []
#     p = []
#     for x in line:
#         if line.count(x) == 2:
#             p.append(x)
#         if line.count(x) == 1:
#             np.append(x)
#     if len(p) == 4 and len(np) == 3:
#         if line.count(max(line)) == 1:
#             print(sum(line))
#             break

# a = []
# for line in open('9.txt'):
#     a.append([int(x) for x in line.split()])
# count = 1
# for line in a:
#     p = []
#     np = []
#     for x in line:
#         if line.count(x) == 2:
#             p.append(x)
#         if line.count(x) == 1:
#             np.append(x)
#     if len(p) == 2 and len(np) == 4:
#         if p[0] >= sum(np) / 4:
#             print(count)
#             break
#     count += 1

# count = 1
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     np = [x for x in a if a.count(x) == 1]
#     p = [x for x in a if a.count(x) == 2]
#     if len(p) == 2 and len(np) == 4:
#         if p[0] >= sum(np) / len(np):
#             print(count)
#             break
#     count += 1


# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if len(a) == len(set(a)):
#         if ((a[0] + a[-1]) * (a[0] + a[-1])) >= (a[1] * a[2] * a[3]):
#             count += 1
# print(count)

# count =0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 4 and len(np) == 3:
#         if (sum(p) / 4) < (sum(a) / 7):
#             count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if (a[4] ** 2) > (a[0] * a[1] * a[2] * a[3]):
#         if (a[3] + a[4]) >= (a[0] + a[1] + a[2]) * 2:
#             count += 1
# print(count)


# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if len(a) == len(set(a)):
#         if (a[2] *2) > (a[-1]) and (a[2] *2 > a[0] * 3):
#             count += 1
# print(count)


# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if len(a) == len(set(a)):
#         if (a[0] + a[-1]) * 2 >= (a[1] + a[2] + a[3]):
#             count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     p.sort()
#     if len(set(p)) == 3:
#         if p[0] ** 2 + p[2] ** 2 == p[4] ** 2:
#             count += 1
# print(count)


# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 2 and len(np) == 4:
#         if sum(np) / 4 >= sum(p):
#             count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     ch = [x for x in a if int(x) % 2 != 0]
#     if (len(a) != len(set(a))) != (len(ch) == 3):
#         count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if len(a) == len(set(a)):
#         if max(a) < (sum(a) - max(a)):
#             count += 1
# print(count)


# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 3]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 3 and len(np) == 3:
#         if (sum(np) / len(np)) < sum(p):
#             count += 1
# print(count)






