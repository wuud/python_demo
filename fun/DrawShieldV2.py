import turtle as t
t.tracer(1.5)
def setpen():
    '''
    调整画笔位置
    '''
    t.left(90)
    t.penup()
    t.fd(25)
    t.pendown()
    t.right(90)
t.penup()
t.right(90)
t.fd(200)
t.pendown()
t.left(90)

t.fillcolor("red")
t.pencolor("red")
t.begin_fill()
t.circle(200)
t.end_fill()

setpen()

t.fillcolor("white")
t.pencolor("white")
t.begin_fill()
t.circle(175)
t.end_fill()

setpen()

t.fillcolor("red")
t.pencolor("red")
t.begin_fill()
t.circle(150)
t.end_fill()

setpen()

t.fillcolor("blue")
t.pencolor("blue")
t.begin_fill()
t.circle(125)
t.end_fill()

t.fillcolor("white")
t.pencolor("white")
t.penup()
t.goto(-118,38)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(238)
    t.right(144)
t.end_fill()
t.hideturtle()
t.done()
