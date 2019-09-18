def add(a,b):
    print('a={:b},b={:b}'.format(a,b))
    if b==0:
        return a
    return add(a^b,(a&b)<<1)
print(add(13,6))