#sum(map(int, n))
#
# def f(N):
#     n = bin(N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     R = int(n, 2)
#     return  R
#
# N = 1
# while True:
#     if f(N) > 77:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     R = int(n, 2)
#     return R
#
# N = 1
# while True:
#     if f(N) > 80:
#         print(N)
#         break
#     N += 1



# def f(N):
#     n = bin(N)[2:]
#     if n.count('1') > n.count('0'):
#         n += '0'
#     else:
#         n = '11' + n
#
#     if n.count('1') > n.count('0'):
#         n += '0'
#     else:
#         n = '11' + n
#     return int(n , 2)
#
# N = 1
# while True:
#     if f(N) > 500:
#         print(N)
#         break
#     N += 1

# def f(N):
#     n = bin(N)[2:]
#     if n[-1] == '0':
#         n += '1'
#     else:
#         n += '0'
#
#     if n[-1] == '0':
#         n += '1'
#     else:
#         n += '0'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) < 171:
#         print(N)
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     if n[-1] == '1':
#         n += '0'
#     else:
#         n = '1' + n
#
#     if n.count('1') % 2 == 0:
#         n += '1'
#     else:
#         n += '0'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) > 228:
#         print(N)
#         break
#     N += 1

# инверсия

# def f(N):
#     n = bin(N)[2:]
#     n = n.zfill(8)
#     n = n.replace('1', '2'). replace('0', '1').replace('2', '0')
#     R = int(n, 2) + 1
#     return R
#
# N = 1
# while True:
#     if f(N) == 221:
#         print(N)
#         break
#     N += 1

# def f(N):
#     n = bin(N)[2:]
#     if n[-1] == '0':
#         n = '10' + n
#     else:
#         n = '11' + n
#
#     if str(n.count('1') % 2) != 0:
#         n += '11'
#     else:
#         n += '00'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) < 860:
#         print(N)
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     R = int(n, 2)
#     return R
#
# N = 1
# while True:
#     if f(N) > 170:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     if str(n.count('1') % 2) != 0:
#         n += '11'
#     else:
#         n += '00'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) > 114:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     if sum(map(int, n)) % 2 == 0:
#         n += '00'
#     else:
#         n += '11'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) > 115:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     n = str(n)
#     n += n[1] + n[0]
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) > 90:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     if sum(map(int, n)) % 2 == 0:
#         n += '01'
#     else:
#         n += '10'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) > 73:
#         print(N)
#         break
#     N += 1














