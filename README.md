a=int(input("enetr the A value:"))
b=int(input("enter the B value:"))
print("Addition press-->1")
print("Subtraction press-->2")
print("Multipication press-->3")
print("Division press-->4")
print("Modulus press-->5")
print("Floor division press-->6")
print("Exponentiation press-->7")
class parent():
    def add(self):
        c=a+b
        print(c)
class parent1(parent):
    def sub(self):
        c=a-b
        print(c)
class child(parent1):
    def mul(self):
        c=a*b
        print(c)
class child1(child):
    def div(self):
        c=a/b
        print(c)
class child2(child1):
    def mod(self):
        c=a%b
        print(c)
class child3(child2):
    def flo(self):
        c=a//b
        print(c)
class child4(child3):
    def exp(self):
        c=a**b
        print(c)
obj=child4()
choice=int(input("enter the choice:"))
if choice==1:
    obj.add()
elif choice==2:
    obj.sub()
elif choice==3:
    obj.mul()
elif choice==4:
    obj.div()
elif choice==5:
    obj.mod()
elif choice==6:
    obj.flo()    
elif choice==7:
    obj.exp()  
    
        
        
        
