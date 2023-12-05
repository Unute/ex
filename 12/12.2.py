# ms = 0
# for n in range(4, 10000):
#     s = '1' + '2' * n
#     while '12' in s or '322' in s or '222' in s:
#         s = s.replace('12','2',1)
#         s = s.replace('322', '21', 1)
#         s = s.replace('222', '3', 1)
#     sm = sum(map(int, s))
#     ms = max(ms, sm)
# print(ms)

# ms = 0
# for m in range(1000):
#     s = '4' + '6' * m
#     while '46' in s or '666' in s:
#         s = s.replace('46', '5', 1)
#         s = s.replace('666', '4', 1)
#     print(s)
#     if sum(map(int, s)) > 1000:
#         print(m)
#         break

# for t in range(4, 10000):
#     s = '3' + '5' * t
#     while '25' in s or '355' in s or '555' in s:
#         s = s.replace('25', '32', 1)
#         s = s.replace('355', '25', 1)
#         s = s.replace('555', '3', 1)
#     if s.count('22222') == 1:
#         print(s)
#         print(t)
# 39

# for n in range(100):
#     s = '3' + '0' * 40 + '1' * n + '2' * 40
#     while '31' in s or '32' in s or '30' in s:
#         s = s.replace('31', '223', 1)
#         s = s.replace('32', '23', 1)
#         s = s.replace('30', '13', 1)
#     s = s.replace('3', '0', 1)
#     print(sum(map(int ,s)), n)
#     # if len(sum(map(int ,s))) == 3

# for n in range(3, 100):
#     s = '3' + '5' * n
#     while '25' in s or '355' in s or '555' in s:
#         s = s.replace('25', '3', 1)
#         s = s.replace('355', '52', 1)
#         s= s.replace('555', '23', 1)
#     if sum(map(int, s))  == 27:
#         print(n)
#         break

# s = '1' + '0' * 55
# while '1' in s:
#     if '10' in s:
#         s=  s.replace('10', '001', 1)
#     else:
#         s = s.replace('1', '00', 1)
# print(s.count('0'))

# s = '0' + '1' *45
# while '0' in s or '01' in s:
#     if '01' in s:
#         s = s.replace('01', '10', 1)
#     else:
#         s = s.replace('0', '111', 1)
# print(s.count('1'))

# s = '4' * 60 + '6' * 60 + '8' * 60
# while '46' in s or '84' in s or '86' in s:
#     s = s.replace('46', '64', 1)
#     s = s.replace('84', '48', 1)
#     s = s.replace('86', '68', 1)
# print(s[149])

# for n in range(1, 20):
#     s = '>' + '0' * 37 + '1' * n + '2' * 37
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if  '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#         s = s.replace('>', '')
#     print(sum(map(int, s)), n)


















