def hanoi(n,a,b,c):
    print(a)
    if n==1:
        print(a,"->",c)
    else:
        hanoi(n-1,a,c,b)
        print(a,"->",c)
        hanoi(n-1,b,a,c)
hanoi(3,'a','b','c')
