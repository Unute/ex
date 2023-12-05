from turtle import *

# tracer(0)
# m = 40
# for i in range(7):
#     fd(10 * m)
#     rt(120)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*m ,y*m)
#         dot(5, 'blue')
#
# update()
# input()




# tracer(100)
# m = 9
# up()
# goto(-3 *m, 23 *m)
# down()
#
# for i in range(10):
#     for i2 in range(3):
#         fd(10 *m)
#         rt(90)
#         fd(10 *m)
#         rt(270)
#     rt(90)
#
# up()
# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x *m, y *m)
#         dot(3, 'blue')
# input()


tracer(100)
m = 35

up()
goto(-5*m, -5*m)
down()
for i in range(5):
    for i2 in range(5):
        for i3 in range(5):
            fd(2*m)
            lt(120)
        fd(2*m)
        lt(120)
        fd(2*m)
    fd(2*m)
    lt(120)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'blue')
input()


















