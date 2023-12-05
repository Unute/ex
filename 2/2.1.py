# print('x,y, z, w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x or y) and (not (y == z)) and (not w)
#                 if f == 1:
#                     print(x, y, z, w)

# print('x, y, w, z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x and z) or ((w <= x) == (z <= y))
#                 if f == 0:
#                     print(x, y, w, z)



# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = (x <= (z == w)) or (not(y <= w))
#                 if f == 0:
#                     print(w,x,y,z)


# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(w,x,y,z)

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((x == z) or (not(x == w))) and ((y <= x) or (not z))
#                 if f == 0:
#                     print(x, y, z, w)














