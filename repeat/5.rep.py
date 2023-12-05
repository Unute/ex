# def d(x):
#     st = ''
#     while x > 0:
#         st += str(x % 3)
#         x //= 3
#     return (st[::-1])
#
# def f(N):
#     n = d(N)
#     if int(n) % 3 == 0:
#         n = '1' + n + '02'
#     else:
#         ost = d((int(n) % 3) * 4)
#         n += str(ost)
#     return int(n, 3)
#
# N = 1
# while True:
#     if f(N) <= 199:
#         print(N)
#     N += 1



# def f(N):
#     n = bin(N)[2:]
#     if int(n) % 3 == 0:
#         n += n[-3] + n[-2] + n[-1]
#     else:
#         ost = bin((int(n) % 3) * 3)[2:]
#         n += ost
#     return int(n, 2)
#
# N = 1
# while True :
#     if f(N) < 76:
#         print(N)
#     N += 1





