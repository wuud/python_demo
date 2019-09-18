import turtle as t
t.pensize(15)
t.color("red")
def setPen(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def draw1():
    setPen(0,50)
    t.right(90)
    t.fd(100)
    t.left(90)
def draw2():
    setPen(50,50)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
draw1()
draw2()

