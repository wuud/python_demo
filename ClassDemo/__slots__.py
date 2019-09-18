class Student:
    pass
def setName(self,name):
    self.name=name
#可以为Student类额外绑定方法
Student.setName=setName
a=Student()
a.setName("tom")
print(a.name)

class Student2:
    #可用__slots__特殊变量来限制类实例可添加的属性
    __slots__ = ('age','name')
b=Student2()
b.name="jim"
print(b.name)
print(Student2.__dict__)
