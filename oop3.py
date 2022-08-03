










class Phone: #super class
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def full_spec(self):
        print(f"the full spec of this spec is: {self.brand} {self.model} and price is {self.price}")

class SmartPhone (Phone): #child class
    def __init__(self,ram,memory,camera,brand,model,price):
        super().__init__(brand,model,price)   #super sends to super class
        self.ram = ram
        self.memory = memory
        self.camera = camera

    def full_spec(self):
        print (f"the full spec of this phone is: {self.brand} {self.model} and price is {self.price}")


#creating more class inside phone - flagship phone, low budget phone, 

class FlagshipPhone (SmartPhone):
    def __init__(self,security,ram,memory,camera,brand,model,price):
        super().__init__(ram,memory,camera,brand,model,price)
        self.security= security

    def full_spec(self):
        print (f"the full details of phone is {self.brand}\n {self.model}\n  and price is {self.price}\n with high security {self.security}")

     
phone1 = Phone("maharshi","landline",4500)
sp = SmartPhone(brand="mi",model="note 5",price =45000,ram="3GB",memory="64GB",camera="20MP")
fp = FlagshipPhone(brand="samsung",model="S10+",price=45000,ram="8GB",memory="256GB",camera="100MP",security="kei chaina")



print(fp.brand)
print(sp.brand)
print(sp.full_spec())
print(fp.full_spec())

#print(help(FlagshipPhone))
#print (FlagshipPhone.mro())  #for finding kun kasko bhitra cha..flagship is inside smartphone .....


#THIS IS FOR CLASS AND 
print (isinstance(sp,FlagshipPhone))  #is sp object of flaship no so false 
print (isinstance(sp,Phone))
print (isinstance())



print (issubclass(FlagshipPhone,FlagshipPhone))
print (issubclass(SmartPhone,Phone))
print (issubclass(Phone,FlagshipPhone))
print ()