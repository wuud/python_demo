def fun(str):
    count=1
    for i in range(1,str.__len__()):
        if str[i]==str[i-1]:
            continue
        else:
            count+=1
    return count
str=input()
print('%.2f'%(str.__len__()/fun(str)))

