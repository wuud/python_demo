def f(base):
    def foo(step=1):
        nonlocal base
        base+=step
        return base
    return foo()
a=f(6)
print(a)
