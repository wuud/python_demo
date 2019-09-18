def f(s,**kw):
    print(kw.__dict__)
f(2,age=5)