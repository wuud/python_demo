import turtle as t
#t.tracer(2)
t.pensize(2)
t.pencolor("green")
t.register_shape("捕获.gif")
t.shape("捕获.gif")
def setpen(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
x=-500
n=8
for i in range(10):
    setpen(x,0)
    t.write("python",align="left", font=("Arial", n, "normal"))
    n+=1
    x+=100
def draw_hexagon(length):
    for i in range(6):
        t.fd(length)
        t.left(60)
'''for i in range(36):
    t.left(i*10)
    draw_hexagon(100)
    setpen(x,y)'''

t.hideturtle()
t.done()

