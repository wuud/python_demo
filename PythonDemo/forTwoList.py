
'''
利用zip()方法可实现多个列表的一次性遍历，如下：
'''

name_list=['w','s','a','d']
id_list=[2,5,7,1]
sex_list=['m','w','w','m']
for i,j,s in zip(name_list,id_list,sex_list):
    print(i,j,s)