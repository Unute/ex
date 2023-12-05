from turtle import *

tracer(4)
m = 13
up()
goto(-5 * m, 15 *m)
down()

for i in range(70):
    fd(8 * m)
    rt(30)

up()
for x in range(-18, 18):
    for y in range(-18, 18):
        goto(x * m, y * m)
        dot( 3, 'blue')

input()