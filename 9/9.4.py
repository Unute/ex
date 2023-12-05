

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 4 and len(np) == 3:
#         if (sum(p) / len(p)) < (sum(a) / len(a)):
#             count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if len(a) == len(set(a)):
#         if (a[2] * 2) > a[-1] and (a[2] * 2) > (a[0] * 3):
#             count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     a.sort()
#     if len(p) == 6:
#         if (a[5] ** 2) == ((a[0] ** 2) + a[2] ** 2):
#             count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     nech = [x for x in a if x % 2 != 0]
#     p = [x for x in a if a.count(x) >= 2]
#     if (len(p) >= 2) + (len(nech) == 3) == 1:
#         count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     a.sort()
#     if (len(a) == len(set(a))) + ((sum(a) - a[-1]) < a[-1]) == 1:
#         count += 1
# print(count)

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 3]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 3 and len(np) == 4:
#         if (sum(np) / 4) <= (sum(p) / 3):
#             count += 1
# print(count)

# k = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     a.sort()
#     k += 1
#     if len(p) == 4 and len(np) == 3:
#         if a.count(a[-1]) == 1:
#             print(k, a, sum(map(int, a)))

# count = 0
# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     tri = [x for x in a if abs(x) % 10 == 3]
#     otr = [x for x in a if x < 0]
#     pol = [x for x in a if x > 0]
#     if len(tri) == 3:
#         if ((sum(otr)) ** 2) > (sum(pol) ** 2):
#             count += 1
# print(count)

count = 0
for line in open('9.txt'):
    a = [int(x) for x in line.split()]
    p = [x for x in a if a.count(x) == 3]
    np = [x for x in a if a.count(x) == 1]
    if (sorted(a) == a) + (len(p) == 3 and len(np) == 4) <= 1:
        count += 1
print(count)