# s = кол-во камней
# c = номер хода
# m = сколько ходов в игре рассматриваем
# def f(s, c, m):
#     if s >= 47: return c % 2 == m % 2
#     if c == m: return 0
#     h= [f(s + 1, c + 1, m), f(s * 3, c + 1 ,m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
# если неудачный ход то any
# for s in range(1, 47):
#     for m in range(1,5):
#         if f(s, 0 ,m):
#             if m == 2:
#                 print(s,m)
#             break
# 19 ответ 6

# for s in range(1, 47):
#     for m in range(1,5):
#         if f(s, 0 ,m):
#             if m == 3:
#                 print(s,m)
#             break
#20 ответ 5 14

# for s in range(1, 47):
#     for m in range(1,5):
#         if f(s, 0 ,m):
#             if m == 4:
#                 print(s,m)
#             break
#  21 ответ 13


# def f(s, c, m):
#     if s >= 47: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 47):
#     for m in range(1,5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)

# 19: 12
# 20: 2122
# 21: 20




# две кучи камней

# def f(a, b, c, m):
#     if a + b >= 107: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(a + 1, b, c+ 1, m), f(a, b + 1, c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1,94):
#     for m in range(1, 5):
#         if f(13, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

# 19: 24
# 20: 4046
# 21: 39

# def f(s, c, m):
#     if s >= 111: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 3, c+  1, m), f(s * 4, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 111):
#     for m in range(1, 5):
#         if f(s, 0 ,m):
#             if m == 4 :
#                 print(s, m)
#             break

# 19: 27
# 20: 2426
# 21: 23


# def f(s, c, m):
#     if s >= 59: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 3, c + 1, m), f(s * 4, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 59):
#     for m in range(1,5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

# 19: 14
# 20: 11 13
# 21: 10

# def f(s, c, m):
#     if s >= 43: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 43):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

# def f(s, c, m):
#     if s >= 348: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 2, c + 1, m), f(s + 4, c + 1,m), f(s * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 347):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break










