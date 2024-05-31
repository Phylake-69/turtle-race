import turtle
from random import *
from turtle import *

penup()
goto(-140, 140)

for sp in range(15):
    speed(10)
    write(sp)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

rex = Turtle()
rex.color("red")
rex.shape('turtle')
rex.penup()
rex.goto(-160, 80)
rex.pendown()

tex = Turtle()
tex.color("blue")
tex.shape('turtle')
tex.penup()
tex.goto(-160, 60)
tex.pendown()

dex = Turtle()
dex.color("green")
dex.shape('turtle')
dex.penup()
dex.goto(-160, 40)
dex.pendown()

for turn in range(100):
    rex.forward(randint(1, 5))
    tex.forward(randint(1, 5))
    dex.forward(randint(1, 5))

turtle.done()
