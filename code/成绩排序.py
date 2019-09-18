n=eval(input())
m=eval(input())
d={}
keys=[]
for i in range(n):
    value,key=input().split()
    d[eval(key)]=value
    keys.append(eval(key))
print(keys)
if m==1:
    keys=sorted(keys)
    print(keys)
    for i in keys:
        print("{} {}".format(d.get(i),i))
else:
    keys=sorted(keys,reverse=True)
    for i in keys:
        print("{} {}".format(d.get(i),i))

