class Car:
    def __init__(self,name,model,color,long) :
        self.name=name
        self.model=model
        self.color=color
        self.long=long
    def get_info(self):
        return f"name:{self.name}, color:{self.color},  kilometr:{self.long}"
    
    
car1=Car('Cobalt','Chevrolet','white',0)
print(car1.get_info())
