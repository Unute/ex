# def f(N):
#     n = bin(N)[2:]
#     if int(n) % 3 == 0:
#         n += n[-3:]
#     if int(n) % 3 != 0:
#         ost = (int(n) % 3) * 3
#         ost = bin(ost)[2:]
#         n += ost
#     return int(n, 2)
#
# N = 4
# while True:
#     if f(N) > 151:
#         print(f(N), N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     if int(n) % 5 ==0:
#         n = '1' + n + n[-2] + n[-3]
#     else:
#         ost = int(n) % 5
#         ost = bin(ost)[2:]
#         n += ost
#     return int(n, 2)
#
# N = 3
# while True:
#     if f(N) <= 223:
#         print(f(N), N)
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     if sum(map(int, n)) % 4 == 0:
#         n = '10' + n
#     else:
#         n = '11' + n
#     if int(n) % 2 != 0:
#         n += '0'
#     else:
#         n += '1'
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) <= 250:
#         print(N)
#     N += 1



# def g(x):
#     s = ''
#     while x > 0:
#         s += str(x % 8)
#         x //= 8
#     return s[::-1]
#
# def f(N):
#     n = g(N)
#     if int(n) % 7 == 0:
#         n += n[-2:]
#     else:
#         ost = (int(n) % 7) * 7
#         ost = g(ost)
#         n += ost
#     return int(n, 8)
#
# N = 2
# a = set()
# while True:
#     if f(N) < 3000:
#         a.add(f(N))
#         print(len(a))
#     N += 1

# def f(N):
#     n = bin(N)[2:]
#     if N % 5 == 0:
#         n += n[-3] + n[-2] + n[-1]
#     else:
#         ost = (N % 5) * 5
#         ost = bin(ost)[2:]
#         n += ost
#     return int(n , 2)
# print(f(8))
# N = 3
# while True:
#     if f(N) > 256:
#         print(f(N))
#         print(N)
#         break
#     N += 1




# def f(N):
#     n = bin(N)[2:]
#     if int(n) % 5 == 0:
#         n += bin(5)[2:]
#     else:
#         n += '1'
#     if int(n) % 7 == 0:
#         n += bin(7)[2:]
#     else:
#         n += '1'
#     return int(n, 2)
#
# N = 0
# while True:
#     if f(N) < 1855663:
#         print(f(N))
#         print(N)
#     N += 1

