'''
constructor is a special method that get automatically called/invoked when an object is created
purpose-Initialize object attributes,Assign initial values to the variable
perform initial setup
'''

# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("Constructor created")
#     def display(self):
#         print("Parent method")
#         print(self.name,self.age)
#
# p=Parent("Varsha",20)
# p.display()
# p1=Parent("Anandhu",30)
# p1.display()

#Destructor
'''
It is a special method python may call when an object is about to be destroyed
Purpose-perform cleanup operation,close files or connections
'''
class Parent:
    x=1
    def __init__(self):
        print("Constructor created")
    def __del__(self):
        print("Distructor created")


p=Parent()
del p
print(p.x)