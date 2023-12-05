from itertools import product, permutations

# a = list(product('абвеоу', repeat = 3))
# f = list(product('аеоу', repeat = 3))
# for x in a:
#     x = ''.join(x)
#     if all(''.join(s) not in x for s in f):
#         print(x)

# a = list(product('елмру', repeat = 4))
# k = 0
# for x in a:
#     k += 1
#     x = ''.join(x)
#     if x[0] == 'л':
#         print(k, x)

# a = list(product('агмнсту', repeat = 6))
# k = 0
# for x in a:
#     k += 1
#     x = ''.join(x)
#     if x[0] != 'у' and x.count('м') == 2 and x.count('г') <= 1:
#         print(k, x)

# a = list(product('екмопртью', repeat = 5))
# k = 0
# for x in a:
#     k += 1
#     x = ''.join(x)
#     if k % 2 != 0 and x[0] != 'ь' and x.count('к') == 2:
#         print(k, x)

# a = list(product('ьрплеа', repeat = 5))
# k = 0
# count = 0
# for x in a:
#     k += 1
#     x = ''.join(x)
#     if x[-1] == 'ь' and k <= 387:
#         count += 1
#         print(k,x, count)

# a = list(product('гепард', repeat = 5))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x.count('г') == 1 and x[0] != 'а' and x[-1] != 'е':
#         count += 1
# print(count)

# аия нст
# a = list(set(permutations('анастасия', r = 9)))
# f1 = list(product('аия', repeat = 3))
# f2 = list(product('нст', repeat = 3))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if not (any(''.join(s) in x for s in f1) and any(''.join(b) in x for b in f2)):
#         count += 1
# print(count)


# a = list(permutations('0123456789ABCDEF', r = 3))
# ch = list(product('02468ACE', repeat = 2)) + list(product('13579BDF', repeat = 2))
# nch = list(product('13579BDF', repeat = 2))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if all(''.join(s) not in x for s in ch) and x[0] != '0':
#         print(x)
#         count += 1
# print(count)

# a = list(product('01234567', repeat = 5))
# f = list(permutations('16',r = 2)) + list(permutations('36',r = 2)) + list(permutations('56',r = 2)) + list(permutations('76',r = 2))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if all(''.join(s) not in x for s in f) and x.count('6') == 1 and x[0] != '0':
#         count += 1
# print(count)


a = list(permutations('01234567', r = 5))
f = list(product('0246', repeat = 2)) + list(product('1357', repeat = 2))
count = 0
for x in a:
    x = ''.join(x)
    if '1' not in x and all(''.join(s) not in x for s in f) and x[0] != '0':
        count += 1
print(count)
