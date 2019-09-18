#筛选出列表中的回数

#生成一个1到1000的数字列表
lis=[ i for i in range(200)]
def is_palindrome(n):
    s=str(n)
    for i in range(s.__len__()):
        if s[i]==s[s.__len__()-1-i]:
            return True
        else:
            return False
print(list(filter(is_palindrome,lis)))
print(is_palindrome('adssda'))