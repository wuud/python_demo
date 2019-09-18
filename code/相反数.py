def rev(n):
    s=str(n)
    n=int(s[::-1])
    return n
n=eval(input())
print(rev(n)+n)
