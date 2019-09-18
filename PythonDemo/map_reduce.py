from functools import reduce
#map用法，写一个序列化方法，利用map函数让列表内的元素变规范
names=['adam', 'LISA', 'barT']
def normalize(name):
    return name[0].upper()+name[1:].lower()
print(list(map(normalize,names)))
#reduce用法,用reduce计算列表所有书的乘积
lis=[3,5,7,9]
def mul(x,y):
    return x*y
def prod(l):
    return reduce(mul,l)
print(prod(lis))
