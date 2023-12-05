#
# def f(a, b, m, k=''):
#     if a + b >= 100 : return m % 2 == 0
#     if m == 0: return 0
#     h = []
#     if k != 'a + 1': h.append(f(a + 1, b, m - 1, 'a + 1'))
#     if k != 'b + 1': h.append(f(a, b + 1, m - 1, 'b + 1'))
#     if k != 'a + 2': h.append(f(a + 2, b, m - 1, 'a + 2'))
#     if k != 'b + 2': h.append(f(a, b + 2, m - 1, 'b + 2'))
#     if k != 'a + 3': h.append(f(a + 3, b, m - 1, 'a + 3'))
#     if k != 'b + 3': h.append(f(a, b + 3, m - 1, 'b + 3'))
#     if k != 'a + 1': h.append(f(a * 2, b, m - 1, 'a * 2'))
#     if k != 'b * 2': h.append(f(a, b * 2, m - 1, 'b * 2'))
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 98) if f(2, s, 2)]) # 46
# print('20)', [s for s in range(1, 98) if not f(2, s, 1) and f(2, s, 3)]) # 25 48
# print('21)', len([s for s in range(1, 98) if not f(2, s, 1) and not f(2, s, 3) and f(2, s, 5)]))#

# def f(s, m, k='', k2=''):
#     if s >= 21: return m % 2 == 0
#     if m == 0: return 0
#     h = []
#     if k2 != '+1': h.append(f(s + 1, m - 1, '+1', k))
#     if k2 != '+2': h.append(f(s + 2, m - 1, '+2', k))
#     if k2 != '*2': h.append(f(s * 2, m - 1, '*2', k))
#    # h = [f(s + 1, m - 1, '+1', k), f(s + 2, m - 1, '+2', k), f(s * 2, m - 1, '*2', k)]
#     return all(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 21) if not f(s, 1) and f(s, 3)])
# print('20)', [s for s in range(1, 21) if not f(s, 2) and f(s, 4)])
# print('21)', [s for s in range(1, 21) if not f(s, 1) and not f(s, 3) and f(s, 5)])


# def f(s, m):
#     if 72 >= s >= 43:return m % 2 == 0
#     if s > 72: return m % 2 != 0
#     if m == 0: return 0
#     h = [f(s + 1, m - 1), f(s * 2, m - 1), f(s * 3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 43) if f(s, 2)])
# print('20)', [s for s in range(1, 43) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 43) if not f(s, 2) and f(s, 4)])


# def f(s, m):
#     if s >= 55 : return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 55) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 55) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 55) if not f(s, 2) and f(s, 4)])

# def f(s, m, k='', k2=''):
#     if s >= 29: return m % 2 == 0
#     if m == 0: return 0
#     h = []
#     if k2 != '+1': h.append(f(s + 1, m - 1, '+1', k))
#     if k2 != '+2': h.append(f(s + 2, m - 1, '+2', k))
#     if k2 != '*2': h.append(f(s * 2, m - 1, '*2', k))
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 29) if not f(s, 1) and f(s, 3)])
# print('20)', [s for s in range(1, 29) if not f(s, 2) and f(s, 4)])
# print('21)', [s for s in range(1, 29) if not f(s, 1) and not f(s, 3) and f(s, 5)])

# def f(s, m):
#     if s <= 12: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(int(s / 3), m - 1), f(s - 12, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(13, 300) if f(s, 2)]) # 116
# print('20)', [s for s in range(13, 200) if not f(s, 1) and f(s, 3)])#51 152
# print('21)', len([s for s in range(13, 200) if not f(s, 2) and f(s, 4)]))# 24


# def f(a, b, m):
#     if a == b: return m % 2 == 0
#     if m == 0: return 0
#     h = []
#     if a < b: h.append(f(a + 1, b, m - 1)) or h.append(f(a + 3, b, m  - 1))
#     if a > b: h.append(f(a, b + 1, m - 1)) or h.append(f(a, b + 3, m  - 1))
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 24) if not f(13, s, 1) and f(13, s, 2)]) # 9
# print('20)', [s for s in range(1, 24) if not f(13, s, 1) and f(13 ,s , 3)]) # 6 8
# print('21)', [s for s in range(1, 24) if not f(13, s, 2) and f(13, s, 4)])


# def f(s, m):
#     if 50 <= s: return m % 2 == 0
#     if s <= 119: m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 2, m - 1), f(s * 3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 50) if f(s, 2)])
print('20)', [s for s in range(1, 50) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 50) if not f(s, 2) and f(s, 4)])