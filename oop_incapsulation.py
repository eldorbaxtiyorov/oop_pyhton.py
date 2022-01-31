class Person:
    def __init__(self,name,age) :
        print("Init ishladi")
        self.__name=name
        self.age=age
        
    def __str__(self) :
        return f"{self.__name} {self.age}"
    
    def getAge(self):
        return self.__age
    @property
    def age(self):
        return self.__age
    
    def setAge(self,age):
        if age>0 and age<=120:
            self.__age=age
    @age.setter
    def age(self, age):
        print("set age",age)
        if age>0 and age<=120:
            self.__age=age
        else:
            self.__age=None
        
tom=Person('Tom',230)
tom.age=200
print(tom)
