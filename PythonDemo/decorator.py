import time
def log(func):
    def wrapper(*args,**kw):
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
        return func(*args,**kw)
    return wrapper
@log
def f():
    print("hello,world")
f()