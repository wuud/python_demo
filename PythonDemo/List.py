#set集合
set=set()
print(set)
set.add(5)
set.add("k")
print(set)
#list列表

list=[]
list+=[1,2,3,4,5]
list.insert(2,7)

list.append(6)

print(list.index(7))
print(7 in list)
del list[2]
print(list)
print(len(list))


#将列表转换为元组类型
l=tuple(list)
print(l)
#元组
yz=(1,2,3,4,5)
print(yz)
print(yz[::-1])

