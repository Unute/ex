# from fnmatch import fnmatch
#
# for x in range(500001, 501000):
#     D = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             D.add(d)
#             D.add(x // d)
#     if fnmatch(str(sum(D)), '*7?'):
#         print(x, sum(D))

from fnmatch import fnmatch
#
# for x in range(1, 10**6 + 1):
#     D = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             if fnmatch(str(d), '4*'):
#                 D.add(d)
#             if fnmatch(str(x // d), '4*'):
#                 D.add(x // d)
#     if len(D) == 24:
#         print(x, max(D))


# for x in range(5*10**5, 10**6+ 1):
#     D = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             if 1000 <= d <= 9999 and d % 10 == 0:
#                 D.add(d)
#             if 1000 <= (x // d) <= 9999 and (x // d) % 10 == 0:
#                 D.add(x// d)
#     if len(D) > 45:
#         print(x, len(D))

# for x in range(53, 10**7 + 1, 53):
#     if fnmatch(str(x), '*2?2*') and str(x) == str(x)[::-1]:
#         D = set()
#         for d in range(1, int(x ** 0.5) + 1):
#             if x % d == 0:
#                 D.add(d)
#                 D.add(x // d)
#         if len(D) > 30:
#             print(x, sum(D))

# count = 0
# for x in range(0, 10**10 + 1, 4546):
#     if fnmatch(str(x), '8*80*06'):
#         count += 1
#         if count % 60 == 1:
#             print(x, x // 4546)

# for x in range(55000000, 60000000):
#     D = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             if d % 2 != 0:
#                 D.add(d)
#             if (x // d) % 2 != 0:
#                 D.add(x // d)
#             if len(D) > 5:
#                 break
#     if len(D) == 5:
#         print(x, max(D))

# for x in range(10** 9, 5*10**9):
#     if fnmatch(str(x), '1*2*7*04'):
#         D = set()
#         for d in range(1, int(x ** 0.5) + 1):
#             if x % d == 0:
#                 D.add(d)
#                 D.add(x // d)
#         if len(D) == 45:
#             print(x, max(D))

# for x in range(15308, 10**9 + 1):
#     if fnmatch(str(x), '15*3*09'):
#         D = set()
#         for d in range(1, int(x ** 0.5) + 1):
#             if x % d == 0:
#                 D.add(d)
#                 D.add(x // d)
#         if len(D) == 9 :
#             print(x, sorted(D)[-2])


# for x in range(65000, 609755):
#     if fnmatch(str(x), '6*97*5?'):
#         D= set()
#         for d in range(1, int(x ** 0.5) + 1):
#             if x % d == 0:
#                 if d % 2 == 0:
#                     D.add(d)
#                 if (x // d) % 2 == 0:
#                     D.add(x // d)
#         if len(D) >= 4:
#             print(x, sum(D), end=' ')

# for x in range(0, 10** 7 + 1, 53):
#     if fnmatch(str(x), '*2?2*') and str(x) == str(x)[::-1]:
#         D= set()
#         for d in range(1, int(x ** 0.5) + 1):
#             if x % d == 0:
#                 D.add(d)
#                 D.add(x // d)
#         if len(D) > 30:
#             print(x, sum(D), end=' ')

# def f(x):
#     for d in range(2, int(x ** 0.5)):
#         if x % d == 0: return False
#     return True
#
# for x in range(3408698 ,3488710):
#     if fnmatch(str(x), '34?8*9'):
#         D = set()
#         for d in range(2, int(x ** 0.5)):
#             if x % d == 0:
#                 if f(d):
#                     D.add(d)
#                 # if f(x // d):
#                 #     D.add(x // d)
#         if len(D) > 4:
#             print(x, max(D))