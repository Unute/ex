# a = [int(x) for x in range(open('17.txt'))]
# m = -float('inf')
# count = 0
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if abs(a[i] - a[j]) % 60 == 0 and (a[i] % 15 == 0 or a[j] % 15 == 0):
#             count += 1
#             m = max(m, abs(a[i] - a[j]))

# a = [int(x) for x in open('17.txt')]
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if (j - i == 3) and ((abs(a[i]) % 100 == 13) != (abs(a[j]) % 100 == 13)):
#             count += 1
#             m = max(m, a[i] + a[j])
# print(count, m)


# a = [int(x) for x in open('17.txt')]
# count = 0
# m = -float('inf')
# mn = min(x for x in a if 100 <= x <= 999 and x % 10 == 3)
# for i in range(len(a) - 1):
#     if ((1000 <= a[i] <= 9999) + (1000 <= a[i + 1] <= 9999)) == 1:
#         if (a[i] ** 2 + a[i + 1] ** 2) % mn == 0:
#             count += 1
#             m = max(m, a[i] ** 2 + a[i + 1] ** 2)
# print(count, m)


# a = [int(x) for x in open('17.txt')]
# count = 0
# m = -float('inf')
# mx = max(x for x in a if x % 100 == 13)
# for i in range(len(a) - 2):
#     if ((100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999) + (100 <= a[i + 2] <= 999)) == 2:
#         if (a[i] + a[i + 1] + a[i + 2]) <= mx:
#             count += 1
#             m = max(m, a[i] + a[i + 1] + a[i + 2])
# print(count, m)


# a = [int(x) for x in open('17.txt')]
# count = 0
# m = float('inf')
# mn = float('inf')
# # for i in range(len(a) - 1):
# #     if ((abs(a[i] % 10 == 3)) + (abs(a[i + 1] % 10 == 3))) == 1:
# #         m = min(m, a[i], a[i + 1])
# m = 282
# print(m)
# for i in range(len(a)):
#     if '3' in str(a[i]) and a[i] >= m:
#         count += 1
#         mn = min(mn, a[i])
# print(count, mn)


# a = [int(x) for x in open('17.txt')]
# m = -float('inf')
# count = 0
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if a[i] * a[j] % 10 == 0:
#             count += 1
#             m = max(m, a[i] + a[j])
# print(count, m)


# a = [int(x) for x in open('17.txt')]
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if ((a[i] - a[j]) % 2 == 0) and ((a[i] % 31 == 0) or (a[j] % 31 == 0)):
#             count += 1
#             m = max(m, a[i] + a[j])
# print(count, m)





