# def f(a, b ,c ,m):
#     if a + b >= 211: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a *2, b, c+ 1, m), f(a, b* 2, c+ 1,m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 193):
#     for m in range(1, 5):
#         if f(17, s, 0, m):
#             if m == 4:
#                 print(s)
#             break


# def f(a, b, c, m):
#     if a+ b >= 223: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 205):
#     for m in range(1,5):
#         if f(17, s, 0, m):
#             if m == 4:
#                 print(s)
#             break



# def  f(s, c ,m):
#     if s >= 250: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m), f(s + 3, c + 1, m), f(s * 2, c + 1, m), f(s * 3, c + 1, m), f(s ** 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 251):
#     for m in range(1,5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s)
#             break

# def f(a, b ,c ,m):
#     if a + b >= 247: return c % 2== m % 2
#     if c == m: return 0
#     h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a *2, b, c + 1, m), f(a, b * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 229):
#     for m in range(1, 5):
#         if f(17, s, 0, m):
#             if m == 4:
#                 print(s)
#             break


# def f(a, b, c, m):
#     if a + b >= 200: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(a + 6, b ,c+ 1, m), f(a, b + 6, c+ 1, m), f(a **2, b, c + 1, m), f(a, b ** 2, c+ 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
# for s in range(1, 194):
#     for m in range(1,7):
#         if f(3, s, 0 ,m):
#             if m == 6:
#                 print(s)
#             break

# def f(s, c, m):
#     if s >= 125: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 2, c + 1, m), f(s + 4, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
# for s in range(1, 124):
#     for m in range(1,5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break








