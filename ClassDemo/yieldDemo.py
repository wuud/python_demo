'''
一个函数中一旦有yield，这个函数就成了一个Generator，
所以函数在调用的时候并不会立即执行，只有调用.__next__()或
.send()方法时函数才会执行到yield对应的地方，每调用一次
next函数就执行到下一个yield所在地。
'''

def f():
    print("my demo")
    m=yield 1#yield后面的值赋给了n.__next__(),而此时m是None，send()方法才是给m赋值的
    print(m)
    print("t")
    n=yield 2

n=f()
n.__next__()
n.__next__()
#n.send("run")

