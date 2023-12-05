# for x in '0123456789ABCDE':
#     s = int('97968' + x + '13', 15) + int('7' + x + '213', 15)
#     if s % 14 == 0:
#         print(s // 14)

# for x in '0123456789ABCDE':
#     s = int('97968' + x + '15', 15) + int('7' + x + '233', 15)
#     if s % 14 == 0:
#         print(x, s // 14)

# for x in '0123456789ABCDEFGHI':
#     s = int('A3' + x + '74', 19) + int(x + '40846', 19)
#     if s % 9 == 0:
#         print(x, s // 9)

# for x in '0123456789ABCDEFGH':
#     s = int('77968' + x + '11', 18) + int('4' + x + '213', 18)
#     if s % 7 == 0:
#         print(x, s // 7)

# for x in '0123456789ABCDE':
#     s = int('1' + x + '51', 15) - int('3' + x +'2', 15)
#     if s % 4 == 0:
#         print(s // 4)

# for x in '0123456789ABCDEF':
#     s = int('1F3B' + x + '75', 16) + int('5D' + x + '3B', 16)
#     if s % 11 == 0:
#         print(s // 11)


# for x in '0123456789ABCDEFGHIJ':
#     s = int('627' + x + 'J8', 20) + int('H45I' + x + '5HIJ', 20) + int('4IDB49J' + x + '7', 20)
#     if s % 19 == 0:
#         print(s // 19)
# for a in range(100):
#     print(a, chr(a))

# for x in '0123456789ABCDE':
#     for y in '0123456789ABCDEFG':
#         s = int('123' + x + '5', 15) + int('67' + y + '9', 17)
#         if s % 131 == 0:
#             print(x, y, s // 131)

# for a in range(100):
#     print(a, chr(a))

count = 0
for x in '0123456789ABCDEFGH':
    for y in '0123456789':
        if x > y:
            s = int('5' + x + y + 'A', 18) + int('18' + x + '7', int(y))
            print(s)

# for x in range(1000):
#     s = int('3364' + str(x), 11) + int(str(x) + '7946', 12)
#     s1 = int('55' + str(x) + '87', 14)
#     if s == s1:
#         print(x, s1)