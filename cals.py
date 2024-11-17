a=int(input("enter the number"))
b=int(input("enter the number")) 
def add():
    add=a+b
    print("addition value:",add)
def sub():
    sub=a-b
    print("addition value:",sub)
def mul():
    mul=a*b
    print("addition value:",mul)
def div():
    div=a/b
    print("addition value:",div)
print("addition press1")
print("subtraction press2")
print("multiplication press3")
print("division press4")
choice=int(input("enter the choice"))
if choice == 1:
    print(add())
if choice == 2:
    print(sub())
if choice == 3:
    print(mul())                 
if choice == 4:
    print(div())                      
                 
                 
                 
                 

