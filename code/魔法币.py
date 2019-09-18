s = ''
def fun(n):
    global s
    while n != 0:
        if n % 2 == 0:
            f=lambda n:(n-2)/2
            n=f(n)
            s=s+'2'
        else:
            f=lambda n:(n-1)/2
            n=f(n)
            s=s+'1'
n = eval(input())
fun(n)
print(s[::-1])
