from random import random
points=1000*1000
hits=0
for i in range(points+1):
    x,y=random(),random()
    d=pow(x**2+y**2,0.5)
    if d<1:
        hits+=1
pi=4*(hits/points)
print("圆周率为：{}".format(pi))
