# a = [int(x) for x in open('17.txt')]
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)


# a = [int(x) for x in open('17.txt')]
#
# mx = max(x for x in a if abs(x) % 10 == 3)
# m = -float('inf')
# count = 0
# for i in range(len(a) - 1):
#     if (abs(a[i]) % 10 == 3) != (abs(a[i + 1]) % 10 == 3):
#         if (a[i] ** 2 + a[i + 1] ** 2) >= mx ** 2:
#             count += 1
#             m = max(m, a[i] ** 2 + a[i + 1] ** 2)
# print(count, m)

# a = [int(x) for x in open('17.txt')]
#
# mx = max(x for x in a if abs(x) % 100 == 13)
# count = 0
# m = -float('inf')
# for i in range(len(a) - 2):
#     if (100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999)+ (100 <= a[i + 2] <= 999) == 2:
#         if a[i] + a[i + 1] + a[i + 2] <= mx:
#             count += 1
#             m = max(m, a[i] + a[i + 1] + a[i + 2])
# print(count, m)


# count = 0
# m = -float('inf')
# a = [int(x) for x in open('17.txt')]
# mx = max(x for x in a if 1000 <= abs(x) <= 9999 and abs(x) % 100 == 39)
# for i in range(len(a) - 1):
#     if (1000 <= abs(a[i]) <= 9999) != (1000 <= abs(a[i + 1]) <= 9999):
#         if (a[i] + a[i + 1]) ** 2 <= mx ** 2:
#             count += 1
#             m = max(m, a[i] + a[i + 1])
# print(count, m)


# def prost(x):
#     for d in range(2, int(x ** 0.5) + 1):
#         if x % d == 0:
#             return False
#     return True
# a = [int(x) for x in open('17.txt')]
# count = 0
# m = float('inf')
# for i in range(len(a) - 2):
#     if ('3' in str(a[i])) and ('3' in str(a[i + 1])) and ('3' in str(a[i + 2])):
#         if prost(a[i] + a[i + 1] + a[i + 2]):
#             count += 1
#             m = min(m, a[i] + a[i + 1] + a[i + 2])
# print(count, m)


# a = [int(x) for x in open('17.txt')]
# count = 0
# mx = max(x for x in a if abs(x) % 100 == 25)
# m = -float('inf')
# for i in range(len(a) - 2):
#     if (1000 <= abs(a[i]) <= 9999) + (1000 <= abs(a[i + 1]) <= 9999) + (1000 <= abs(a[i + 2]) <= 9999) <= 2:
#         if (a[i] + a[i + 1] + a[i + 2]) <= mx:
#             count += 1
#             m = max(m, a[i] + a[i + 1] + a[i + 2])
# print(count, m)

# a = [int(x) for x in open('17.txt')]
# mx = max(x for x in a if x % 17 == 0)
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     if (a[i] + a[i + 1]) > mx:
#         m = max(m, a[i] + a[i + 1])
#         count += 1
# print(count, m)

# a = [int(x) for x in open('17.txt')]
# count = 0
# mx = max(x for x in a if (100 <= x <= 999))
# m = -float('inf')
# for i in range(len(a) - 1):
#     if (100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999) == 1:
#         if (a[i] + a[i + 1]) % mx == 0:
#             count += 1
#             m = max(m, a[i] + a[i + 1])
# print(count, m)


# a = [int(x) for x in open('17.txt')]
# count = 0
# m = float('inf')
# mx = max(x for x in a if (100 <= x <= 999))
# for i in range(len(a) - 1):
#     if (100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999) == 1:
#         if (a[i] * a[i + 1]) % mx == 0:
#             count += 1
#             m = min(m, a[i] * a[i + 1])
# print(count, m)

# a = [int(x) for x in open('17.txt')]
# count = 0
# m = -float('inf')
# mx = min(x for x in a if x % 5 == 0 and (100 <= x <= 999))
# for i in range(len(a) - 1):
#     if (100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999) >= 1:
#         if (a[i] + a[i + 1]) % mx == 0:
#             count += 1
#             m = max(m, a[i] + a[i + 1])
# print(count, m)

# a = [int(x) for x in open('17.txt')]
# count = 0
# m = -float('inf')
# mx = min(abs(x) for x in a)
# for i in range(len(a) - 1):
#     if (a[i] < 0) + (a[i + 1] < 0) == 1:
#         if ((a[i] + a[i + 1]) > 0) and ((a[i] + a[i + 1]) % mx == 0):
#             count += 1
#             m = max(m, a[i] + a[i + 1])
# print(count, m)


# a = [int(x) for x in open('17.txt')]
# count = 0
# mx = min(x for x in a)
# m = -float('inf')
# for i in range(len(a) - 1):
#     if (a[i] % 117 == mx) + (a[i + 1] % 117 == mx) >= 1:
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)


# a = [int(x) for x in open('17.txt')]
# count = 0
# m = -float('inf')
# mx = max(x for x in a if x % 100 == 54)
# for i in range(len(a) - 1):
#     if str(a[i])[-1] == str(a[i + 1])[-1]:
#         if (abs(a[i]) + abs(a[i + 1])) <= mx:
#             count += 1
#             m = max(m, a[i], a[i + 1])
# print(count, m)












