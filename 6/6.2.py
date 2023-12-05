from turtle import *
# tracer(10)
# m = 25
# up()
# goto(-10*m, 10*m)
# down()
# for i in range(2):
#     fd(13 * m)
#     rt(90)
#     fd(20 * m)
#     rt(90)
# up()
# fd(8*m)
# rt(90)
# fd(-3*m)
# lt(90)
# down()
# for i in range(2):
#     fd(16*m)
#     rt(90)
#     fd(8*m)
#     rt(90)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# input()

tracer(10)
m = 32
# up()
# goto(-7*m,0)
# down()
for i in range(6):
    for j in range(3):
        fd(7*m)
        rt(120)
    rt(60)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'blue')
update()
input()
