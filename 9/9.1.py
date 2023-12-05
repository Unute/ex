# f = open('9.txt').readlines()
# k = 0
# for line in f:
#     a = list(map(int, line.split('	')))
#     count = 0
#     for x in a:
#         if a.count(x) == 2:
#             count += 1
#             x1 = x
#         if count == 2:
#             if (sum(a) - x1 - x1) / 4 <= x1 + x1:
#                 k += 1
# print(k)



# f = open('9.txt').readlines()
# k = 0
# for line in f:
#     a = list(map(int, line.split('	')))
#     count = 0
#     a.sort()
#     if (a[0] + a[-1]) % 3 == 0:
#
#         k += 1
# print(k)



f = open('9.txt').readlines()
for line in f:
    a = list(map(int, line.split('	')))
    a.sort()
    for x in a:
        if a.count(x) == 0:
            if ((x[0] + x[-1]) * 5) >= ((x[1] + x[2] + x[3] + x[4]) * 3):
                print(a)










