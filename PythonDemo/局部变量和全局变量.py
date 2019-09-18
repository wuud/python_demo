a=10
def func(n):
    global a
    a=a+n
    print(a)
func(3)
print(a)
