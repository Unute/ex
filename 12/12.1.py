# s = '8' * 70
# while '2222' in s or '8888' in s:
#     if '2222' in s:
#         s = s.replace('2222', '88', 1)
#     else:
#         s = s.replace('8888', '22', 1)
# print(s)

# s = '2' + '5' * 81
# while '25' in s or'355' in s or '4555' in s:
#     if '25' in s:
#         s = s.replace('25' , '4', 1)
#     if '355' in s:
#         s = s.replace('355', '2', 1)
#     if '4555' in s:
#         s = s.replace('4555', '3', 1)
# print(s)


# s = '4' * 204
# while '4444' in s or '777' in s:
#     if '4444' in s:
#         s = s.replace('4444', '77', 1)
#     else:
#         s = s.replace('777', '4', 1)
# print(s)


for n in range(3, 10000):
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    if sum(map(int, s)) == 64:
        print(n)

# демоверсия

# s = '>' + '1' * 15 + '2' * 20 + '3' * 25
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>1', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>', 1)
# s = s.replace('>', '')
# print(sum(map(int, s)))


# s = '1' * 170 + '3' * 100 + '2' * 7
# while '11' in s:
#     s = s.replace('112', '4', 1)
#     s = s.replace('113', '2', 1)
#     s = s.replace('42', '3', 1)
#     s = s.replace('43', '1', 1)
# print(s)



