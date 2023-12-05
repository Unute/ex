import itertools

# count = 0
# a = list(ir.product('гафний', repeat=4))
# for x in a:
#     if x[0] != 'й' and ('а' in x or 'и' in x):
#         count += 1
# print(count)

# a = list(itertools.product('игра', repeat=5))
# count = 0
# for x in a:
#     if x.count('а') == 2:
#         count += 1
# print(count)

# a = list(itertools.permutations('матвей', r =6))
# count = 0
# for x in a:
#     if x[0] != 'й' and x.count('ае') == 0:
#         count+=1
# print(count)

# a = list(itertools.permutations('левий', r = 5))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x[0] != 'й' and 'еи' not in x:
#         count+=1
# print(count)

# a = list(itertools.product('милена', repeat = 6))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x.count('а') <= 1 and x[0] != 'а' and x[-1] != 'а' and 'ае' not in x:
#         count+=1
# print(count)

# a = list(itertools.product('пир', repeat = 5))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x.count('п') == 1:
#         count += 1
# print(count)

# a = list(itertools.product('abcdx', repeat =4))
# count = 0
# for x in a:
#     if (x[0] == 'x' and x.count('x') == 1) or x.count('x') == 0:
#         count += 1
# print(count)

# a = list(itertools.permutations('ольга', r = 5))
# count = 0
# for x in a:
#     x = ''.join(x)
#     if x[0] != 'ь' and x.count('оь') == 0 and x.count('аь') == 0:
#         count += 1
#         print(x)
# print(count)

# a = list(itertools.product('аимря', repeat = 4))
# n = 1
# for x in a:
#     x = ''.join(x)
#     if x == 'ария':
#         break
#     n+=1
# print(n)

# a = list(itertools.product('аимря', repeat = 4))
# print(a[210])

# a = list(itertools.product('лнрт', repeat = 5))
# print(a[149])

# a = list(itertools.product('влту', repeat = 4))
# print(a[97])

# a = list(itertools.product('аоу', repeat = 5))
# n=1
# for x in a:
#     if x[0] == 'у':
#         break
#     n += 1
# print(n)

# a = list(itertools.product('акру', repeat = 5))
# n=1
# for x in a:
#     if x[0] == 'к':
#         break
#     n+=1
# print(n)

# a= list(itertools.product('кор', repeat = 5))
# print(a[181])

# a= list(itertools.product('апрсу', repeat = 3))
# n=1
# for x in a:
#     if x[0] == 'с':
#         break
#     n+=1
# print(n)


# a= list(itertools.product('амух', repeat = 4))
# n=1
# for x in a:
#     x= ''.join(x)
#     if x == 'хухх':
#         break
#     n+=1
# print(n)


# a = list(itertools.product('авлор', repeat = 4))
# n = 1
# for x in a:
#     if x[0] == 'л':
#         break
#     n+=1
# print(n)



a = list(itertools.product('лето', repeat = 4))

n = 0
for x in a:
    x = ''.join(x)
    if x[0] == 'л' or x[0] == 'т':
        n += 1
    # n += 1
print(n)













