class User:
    def __init__(self,name,username,email) :
        self.name=name
        self.username=username
        self.email=email
    
    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.name}, email: {self.email}"

user1=User("Alijon","alijon007","@alijon123")
print(user1.get_info())


        
