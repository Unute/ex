# x = 49**7 + 7 ** 21 - 7
#
# count = 0
# while x > 0:
#     if x % 7 == 6:
#         count += 1
#     x //= 7
# print(count)

# x = 64**30 + 2**300 -4
#
# count = 0
# while x > 0:
#     if x % 8 == 7:
#         count += 1
#     x //= 8
# print(count)

# x = 81**5 + 3**30 - 27
# count = 0
# while x > 0:
#     if x % 9 == 8:
#         count += 1
#     x //= 9
# print(count)

# x = 9**14 + 3**18 - 9**5 - 27
# count = 0
# while x> 0:
#     if x % 3 == 2:
#         count += 1
#     x //= 3
# print(count)

# x = 8**1023 + 2**1024 - 3
# print(bin(x)[2:].count('1'))



# x = 4**2016 + 2**2018 - 6
# print(bin(x)[2:].count('1'))

# x = 4**350 + 8**340 - 2**320 - 12
# print(bin(x)[2:].count('0'))


# x = 4*125**4 - 25**4 + 9
#
# count = 0
# while x > 0:
#     if x % 5 == 4:
#         count += 1
#     x //= 5
# print(count)


# x = 9**5 + 3**7 - 14
# a0 = 0
# a1 = 0
# a2 = 0
# while x > 0:
#     if x % 3 == 0:
#         a0 += 1
#     if x % 3 == 1:
#         a1 += 1
#     if x % 3 == 2:
#         a2 += 1
#     x //= 3
# print(a0, a1, a2)


# for x in range(0,1000):
#     y = 216**5 + 6**3 - 1 - x
#     s = ''
#     while y != 0:
#         s += str(y % 6)
#         y //= 6
#     s = s[::-1]
#     if s.count('5') == 12:
#         print(x)
#         break


# x = 3 * 3125**8 + 2 * 625 ** 7 - 4 * 625 **6 + 3*125**5 - 2 *25**4 - 2024
# s = ''
# while x > 0:
#     s += str(x % 25)
#     x //= 25
# print(s.count('0'))




# for x in '0123456789abcdefghi':
#     s = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
#     if s % 18 == 0:
#         print(x, s // 18)

# for x in '0123456789abcdefghijklm':
#     s = int('7' + x + '38596', 23) + int('14' + x + '36', 23) + int('61' + x + '7', 23)
#     if s % 22 == 0:
#         print(x, s // 22)


# x = 7*5**123 + 6*5**111 - 5*25**50 + 4*125**30 + 4*125**30 - 3*5**10
# count = 0
# while x != 0:
#     if x % 5 == 4:
#         count += 1
#     x //= 5
# print(count)


# for n in range(6, 20):
#     x = 7 ** 500 - int('53', n)
#     if x % 6 == 0:
#         print(n)
#         break


# for x in '0123456789ABCDEF':
#     s = int('1F3B' + x + '75', 16) + int('5D' + x + '3B', 16)
#     if s % 11 == 0:
#         print(x, s // 11)





# for x in '0123456789abcdefghijkl':
#     a = int('18' + x + '89957', 22) + int('80' + x + '33', 22) + int('521' + x + '6', 22)
#     if a % 21 == 0:
#         print(x, a // 3)


# for x in '0123456789ABCDEF':
#     s = int('1F3B' + x + '75', 16) + int('5D' + x + '3B', 16)
#     if s % 11 == 0:
#         print(x, s // 11)


# for x in '01234567':
#     s = int('2567' + x + '3', 8) + int('1' + x + '24', 8)
#     if s % 7 == 0:
#         print(s, x, s // 7)

# for x in '0123456789ABCDEFGHIJ':
#     for y in '0123456789A':
#         for t in '01234567':
#             try:
#                 s = (int('1' + x + y, 20) + int('3' + y, 11)) / (int('4' + y, 11) - int(t + '1', 8))
#                 if s % 5 == 0:
#                     print(s)
#             except:
#                 ...

# a = set()
# for x in '0123456789ABCDEF':
#     for y in '9ABCDEF':
#         if int(x, 16) < int(y, 16):
#             s1 = int('5' + x + y + 'C', 16)
#             s2 = int('8' + x + x + '7', int(y, 16))
#             a.add(s1 + s2)
# print(len(a))

# x = 4 ** 2015 + 2 ** 2015 - 15
# x = bin(x)
# print(x.count('1'))

# x = 27**4 - 9**5 + 3**8 - 25
# count = 0
# while x > 0:
#     if x % 3 == 2:
#         count += 1
#     x //= 3
# print(count)

# x = 25**56 + 5**138 - 5
# count = 0
# while x > 0:
#     if x % 5 == 4:
#         count += 1
#     x //= 5
# print(count)

# x = 5**2 * 7**25 + 6**2 * 7**36 - 4**2 * 9**3
# count = 0
# while x > 0:
#     if x % 7 == 0:
#         count += 1
#     x //= 7
# print(count)

x = (2**345 + 8**65 - 4**130) * (8**123 - 2**89 + 4**45)
x = oct(x)[2:]
print(sum(map(int, x)))




