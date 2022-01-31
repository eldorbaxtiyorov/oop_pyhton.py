class Shaxs:
    def __init__(self,ism,familiya,passport,tyil) :
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
    def get_info(self):
        info=f"{self.ism} {self.familiya}"
        info+=f"Passport:{self.passport}, tyil:{self.tyil}"
    def get_name(self):
        return f"{self.ism} {self.familiya}"
    def get_age(self,yil):
        return yil-self.tyil
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.fan=[]
    def fanga_yozil(self):
        self.fan.append()
        
class Fan:
    def __init__(self,aniq,tabiy,ijtimoiy,mutaxasislik) :
        self.aniq=aniq
        self.tabiy=tabiy
        self.ijtimoiy=ijtimoiy
        self.mutaxasislik=mutaxasislik

