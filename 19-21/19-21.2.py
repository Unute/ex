# def f(s, m):
#     if s >= 88: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s*3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 88) if f(s, 2)])
# print('20)', [s for s in range(1, 88) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 88) if not f(s, 2) and f(s, 4)])

# def f(a, b, m):
#     if a + b >= 342: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a + 2, b, m - 1), f(a, b + 2, m - 1), f(a * 5, b, m - 1), f(a, b * 5, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 326) if f(11, s, 2)]) # 14
# print('20)', [s for s in range(1, 326) if not f(11, s, 1) and f(11, s, 3)])
# print('21)', [s for s in range(1, 326) if not f(11, s, 2) and f(11, s, 4)])


# def f(s, m):
#     if s >= 273: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 2, m - 1), f(s + 5, m - 1), f(s * 4, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 273) if f(s, 2)]) # 18
# print('20)', [s for s in range(1, 273) if not f(s, 1) and f(s, 3)]) #17 62
# print('21)', [s for s in range(1, 273) if not f(s, 2) and f(s, 4)]) # 60

# def f(s, m):
#     if s >= 281: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 4, m - 1), f(s * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 281) if not f(s, 1) and f(s, 2)]) # 137
# print('20)', [s for s in range(1, 281) if not f(s, 1) and f(s, 3)]) # 69 70
# print('21)', [s for s in range(1, 281) if not f(s, 2) and f(s, 4)] # 129

# def f(s, m):
#     if s >= 111: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 1, m - 1), f(s + 3, m - 1), f(s * 4, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 111) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 111) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 111) if not f(s, 2) and f(s, 4)])

# def f(s, m):
#     if s >= 82: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 2, m - 1), f(s + 4, m - 1), f(s * 3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 82) if f(s, 2)]) #10
# print('20)', [s for s in range(1, 82) if not f(s, 1) and f(s, 3)]) #9 22
# print('21)', [s for s in range(1, 82) if not f(s, 2) and f(s, 4)]) #21