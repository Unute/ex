# x = 49 ** 7 + 7 ** 21 - 7
# count = 0
# while x > 0:
#     if x % 7 == 6:
#         count += 1
#     x //= 7
# print(count)


# x = (7 * (5 ** 123)) + (6 * (5 ** 111)) - (5 * (25 ** 50)) + 4 * 125 ** 30 - 3 * 5 ** 10
# count = 0
# while x > 0:
#     if x % 5 == 4:
#         count += 1
#     x //= 5
# print(count)


# x = 343 ** 515 - 6 * 49** 520 + 5 * 49 ** 510 - 3 * 7 ** 530 - 550
# count = 0
# while x > 0:
#     if x % 7 == 6:
#         count += 1
#     x //= 7
# print(count)



# x = 3* 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156
# count = 0
# while x > 0:
#     if x % 25 == 0:
#         count += 1
#     x //= 25
# print(count)


# x = 2 * 729 ** 1021 - 2 * 243 ** 1022 + 81 ** 1023 - 2 * 27 ** 1024 - 1025
# count = 0
# while x > 0:
#     if x % 3 == 0:
#         count += 1
#     x //= 3
# print(count)





# Операнды

# for x in range(0, 15):
#     c = 1 * 15**4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 ** 1 + 5 * 15 ** 0 + 1 * 15 **4 + x * 15 ** 3 + 2 * 15 ** 2+ 3 * 15 ** 1 + 3 * 15 ** 0
#     if c % 14 == 0:
#         print(c // 14)

for x in range(0,23):
    c = int('738596', 23) + int('14' + x + '36', 23) + int('67' + x '7', 23)
    if c % 22 == 0:
        print(c // 22)





# определить число n
# for n in range(8, 20):
#     if int('103', n) == int('97', n +2 ):
#         print(n)


# for n in range(4, 20):
#     if int('132', n) + int('13', 8) == int('124', n + 1):
#         print(n)



#сколько существует систем счисления

# count = 0
# x = 39
# for n in range(2, 50):
#     if x % n == 3:
#         count += 1
# print(count)







# дз

# for p in range(16):
#     for x in '123456789abcdef':
#         for y in '123456789abcdef':
#             try:
#                 if int('5' + x + '83', p) + int(x + '9' + x + '9', p) == int(y + '20' + y, p):
#                     print(int(x + y+ y+ x, p))
#             except:
#                 ...

# for p in range(16):
#     for x in '0123456789abcdef':
#         for y in '0123456789abcdef':
#             if int('5'+x+'83', p) + int(x+'9'+x+'9', p) == int(y+'20'+y, p):
#                 print(int(x + y + y + x, p))



# count = 0
# for x in range(2 ** 4, 5 ** 4):
#     if x % 16 == 12:
#         count+= 1
# print(count)


# for x in range(0, 7):
#     for y in range(0, 7):
#         try:
#             if int('10' + x +y+x, 6) == int(y+ '11' + x, 7):
#                 print(x+y)
#         except:
#             ...





# for x in range(111):
#     p = 1 * 111 ** 0 + 2 * 111 ** 1 + 3 * 111 ** 2 + x * 111 ** 3 + 4 * 211 ** 0 + x * 211 ** 1 + 7 * 211 ** 2 + 1 * 211 ** 3
#     if p % 111 == 0:
#         print(x)
#         print(p // 111)




# for x in range(67):
#     p =  1 * 81 ** 0 + 2 * 81 ** 1 + x * 81 ** 2 + 3 * 81 ** 3 + 4 * 67 ** 0 + x * 67 ** 1 + 7 * 67 ** 2 + 1 * 67 ** 3
#     if p % 35 == 0:
#         print(p // 35)

# x = 729**6 + 3**14 - 36
# count = 0
# while x > 0:
#     if x % 9 == 0:
#         count += 1
#     x //= 9
# print(count)


x = 6
stg = ''
while x > 0:
    stg += str(x % 3)
    x //= 3
print(stg[::-1])



