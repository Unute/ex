import itertools


# a = list(itertools.permutations('01234567', r = 5))
#
# n = 0
# for x in a:
#     x = ''.join(x)
#     if x[0] != '0' and x.count('1') == 0 and all(c not in x for c in ['02', '04', '06', '20', '24', '26', '40', '42', '46', '60', '62', '64', '13', '15', '17', '31', '35', '37', '51', '53', '57', '71', '73', '75']):
#         print(x)
#         n += 1
# print(n)


# a = list(itertools.product('гафний', repeat = 4))
# n = 0
# for x in a:
#     x = ''.join(x)
#     if x[0] != 'й' and (x.count('а') >= 1 or x.count('и') >= 1):
#         n += 1
# print(n)


# a = list(itertools.product('abcx', repeat = 5))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if (x[-1] == 'x' and x[0] != 'x' and x[1] != 'x' and x[2] != 'x' and x[3] != 'x') or x.count('x') == 0:
#         count += 1
# print(count)


# a = list(itertools.product('аворт', repeat = 6))
# n = 0
# for x in a:
#     x = ''.join(x)
#     n += 1
#     print(n, x)
#     if 'ворота' in x:
#         print(n,x)

# a = list(itertools.product('иклнор', repeat = 4))
# n = 0
# for x in a:
#     x = ''.join(x)
#     n += 1
#     if 'кино' in x:
#         print(n, x)


# a = list(itertools.product('алпця', repeat = 5))
# n = 0
# for x in a:
#     x = ''.join(x)
#     n += 1
#     if x.count('а') == 1 and x.count('ц') == 2 and x.count('л') == 0:
#         print(n ,x)
#         break


a = list(itertools.permutations('012345', r = 5))
n = 0
for x in a:
    x = ''.join(x)
    if all(c not in x for c in ['00', '02', '04', '06', '20', '22', '24', '26', '40', '42', '44', '46', '11', '13', '15', '31', '33', '35', '51', '53', '55']):
        n += 1
print(n)







