# d1, d2, c1, c2 = 17, 58, 29, 80
# d = [i / 10 for i in range(d1 * 10, d2 *10 + 1)]
# c = [i / 10 for i in range(c1 * 10, c2 *10 + 1)]
#
# def f(x, a):
#     return (x in d) <= (((x not in c) and (x not in a)) <= (x not in d))
# a =set()
# for x in [i /10 for i in range(10* 10, 90* 10)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))
# наименьшая длина


# p1, p2, q1, q2 = 44, 49, 28, 53
# p = [i / 10 for i in range(p1 *10, p2*10 + 1)]
# q = [i / 10 for i in range(q1 *10, q2*10 + 1)]
#
# def f(x, a):
#     return ((x in a) <= (x in p)) or (x in q)
#
# a = set([i / 10 for i in range(20 *10, 60 * 10)])
# for x in [i / 10 for i in range(20 *10, 60 * 10)]:
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))
# print(53-28)
# наибольшая длина


# p1, p2, q1, q2 = 13,19,17,23
# p = [i /10 for i in (p1 * 10, p2*10 + 1)]
# q = [i /10 for i in (q1 * 10, q2*10 + 1)]
#
# def f(x, a):
#     return not ((x not in p) <= (x in q)) <= ((x in a) <= (not (x in q) <= (x in p)))
# a = set()
# for x in [i / 10 for i in range(10*10, 30*10)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))

# p1, p2, q1, q2, r1, r2 = 257, 1000, 5, 100, 99, 258
# p = [i /10 for i in range(p1 *10, p2 *10 + 1)]
# q = [i /10 for i in range(q1 *10, q2 *10 + 1)]
# r = [i /10 for i in range(r1 *10, r2 *10 + 1)]
#
# def f(x, a):
#     return ((x in a) <= (x in r)) and (not ((x in a) <= (x in p)) <= (x in q))
#
# a = set()
# for x in [i / 10 for i in range(1*10, 1001*10)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))


# p1,p2,q1,q2,r1,r2 = 5, 280, 295, 400, 375, 450
# p = [i / 10 for i in range(p1 *10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 *10, q2 * 10 + 1)]
# r = [i / 10 for i in range(r1 *10, r2 * 10 + 1)]
#
# def f(x, a):
#     return ((x in q) <= (x in p)) or ((x not in a) <= (x in r))
# a =set()
# for x in [i / 10 for i in range(10, 500 * 10)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))

# p1,p2,q1,q2 = 254, 800, 410, 823
# p = [i / 10 for i in range(p1 *10, p2* 10+ 1)]
# q = [i / 10 for i in range(q1 *10, q2* 10+ 1)]
#
# def f(x, a):
#     return ((x in p) and (x not in a)) <= (x in q)
#
# a = set()
# for x in [i / 10 for i in range(200* 10, 900* 10)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))

# p1,p2,q1,q2 = 69, 91, 77, 114
# p = [i /10 for i in range(p1* 10, p2 *10 + 1)]
# q = [i /10 for i in range(q1* 10, q2 *10 + 1)]
#
# def f(x, a):
#     return (x in q) <= (((x in p) == (x in q)) or ((x not in p) <= (x in a)))
# a = set()
# for x in [i /10 for i in range(60* 10, 120* 10)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))

# p = [1,2,4,8]
# q = [1,2,3,4,5,6]
#
# def f(x, a):
#     return (x not in a) <= (not ((x in p) or (x in q)))
#
# a =set()
# for x in range(0, 20):
#     if not f(x, a):
#         a.add(x)
# print(len(sorted(a)))

# p = [1, 3, 4, 9, 11, 13, 15, 17, 19, 21]
# q = [3, 6, 9 ,12 ,15, 18, 21, 24, 27, 30]
#
# def f(x, a):
#     return ((x in p) <= (x in a)) or ((x not in a) <= (x not in q))
#
# a =set()
# for x in range(0, 40):
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))
# print(3*9*15*21)

# b1,b2,c1,c2 = 23,37,41,73
# b = [i/10 for i in range(b1* 10, b2* 10 + 1)]
# c = [i/10 for i in range(c1* 10, c2* 10 + 1)]
#
# def f(x,a):
#     return not(((x not in b) <= (x in c)) <= (x in a))
# a= set()
# for x in [i /10 for i in range(20* 10, 80* 10)]:
#     if not f(x,a):
#         a.add(x)
# print(sorted(a))

# p = [2,4,6,8,10,12,14,16,18,20]
# q = [3,6,9,12,15,18,21,24,27,30]
# r = [12,21,36,48,60]
#
# def f(x, a):
#     return (x not in a) <= (((x in p) and (x in q)) <= (x in r))
# a =set()
# for x in range(1, 70):
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))
# print(6* 18)

# p = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
# q = [1,4,7,10,13,16,19,22, 25,28,31]
#
# def f(x, a):
#     return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))
#
# a =set(range(0, 40))
# for x in range(0, 40):
#     if not f(x, a):
#         a.remove(x)
# print(len(sorted(a)))

# p = [12,23,34,45,56]
# r = [23,35,56,68,89]
#
# def f(x, a):
#     return (x in p) or (x in r) or (x not in a)
#
# a = set(range(10, 100))
# for x in range(10, 100):
#     if not f(x, a):
#         a.remove(x)
# print(len(sorted(a)))

# p = [3,6,9,12]
# r = [1,2,3,4,5,6]
#
# def f(x, a):
#     return not (( x not in a) and (x in p)) or (x not in r)
# a = set()
# for x in range(1, 15):
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))

# p = [1,3,5,7,9,11]
# r = [3,6,9,12]
# def f(x, a):
#     return ((x in p) <= (x not in r)) or (x in a)
# a =set()
# for x in range(0, 15):
#     if not f(x, a):
#         a.add(x)
#
# print(sorted(a))

# p1,p2,q1,q2,r1,r2 = 257,1000,5,100,99,258
# p = [i / 10 for i in range(p1* 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1* 10, q2 * 10 + 1)]
# r = [i / 10 for i in range(r1* 10, r2 * 10 + 1)]
#
# def f(x, a):
#     return ((x in a) <= (x in r)) and (not ((x in a) <= (x in p))) <= (x in q)
# a =set()
# for x in [i / 10 for i in range(1*10, 1010* 10)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))