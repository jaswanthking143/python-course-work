'''
class Bike:
    name ="r15"
    colour="white"
    cc="150"
    speed="180"
c1 = Bike()
print(c1.name)
print(c1.colour)
print(c1.cc)
print(c1.speed)
 


class Car:
    name= "volva"
    colour='black'
    def speed(self):
        print(self.name)
        print(self.colour)
        print("220KMPH")
c1=Car()
c1.speed()
    



class Student:
    def studentDetails(self):
        print("Hello student")
s1=Student()
print(s1)
s1.studentDetails()


class Student:
    def studentDetails(xyz,name,age):
        print(name,age)
s1=Student()
s1.studentDetails("jaswanth",'21')



class Flipkart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showproducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now!")

ram = Flipkart()
ram.login('ram','ram2003@')
ram.banner()
ram.showproducts()

Flipkart.showproducts()
Flipkart.banner()






class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f'Welcome to the Instagram,{self.username}')

jaswanth = Instagram('jaswanth','jaswanth@123')
'''



class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.followers = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

vamsi = Instagram('vamsi','vamsi@123')

print("Before usrename:",vamsi.username)
vamsi.username = 'ram'
print("After username:",vamsi.username)

print("Before password:",vamsi.getpassword())
vamsi.setpassword('ram@123')
print("After password:",vamsi.getpassword())
