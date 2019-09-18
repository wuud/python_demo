
class MyClass(object):
    x=11
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def getAge(self):
        return self.__age
    @classmethod
    def classmed(cls):
        print("{}.x={}".format(cls.__name__,cls.x))
tom=MyClass('tom',18)
print(tom.getAge())

print(MyClass.__dict__)
print(MyClass.__dir__(tom))
MyClass.classmed()

