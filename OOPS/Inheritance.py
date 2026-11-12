'''
It is the concepts in which one class acquires the properties and methods of
another class. The first class is called as - parent,base,super
The 2nd class is called as child class,subclass,Inherited class(A child can
reuse the code of a parent class without writing it again)
'''
'''
class Parent:
    networth="10cr"
    def skill(self):
        print("Teaching skill")

class Child(Parent):
    def job(self,jobtittle):
        print(f"jobtittle is {jobtittle}")

c=Child()
c.skill()
print(c.networth)
c.job("Engineer")
'''
#Types of inheritance
#1.single inheritance-One parent and one child
#2.Multiple inheritance-Different parent class and single child class
#3.Multi level inheritance-A child class becomes parent class for another class
#4.Hierarchial inheritance->single parent and different child
#5.Hibrid inheritance->it is the combination of 2 or more types of inheritance
#
# #Multiple inheritance
#
# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
#
# c=C()
#
# #Multi-level inheritance
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# c=C()
#Hierarchial inheritance
#
# class Parent():
#     def display(self):
#         print("Parent method")
#
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# c1=Child1()
# c1.display()
# c2=Child2()
# c2.display()

#Multi level inheritance
'''
house="karthika"
class Parent:
    def __init__(self,father):
        self.father=father
    # def details(self,mother):
    #     self.mother=mother
    #     print("Parent details")
class Child1(Parent):
    def details1(self,mother):
        self.mother=mother
        print("child1 details")
class Child2(Child1):
    def __init__(self,father):
        super().__init__(father)
    def details2(self):
        print(f"Child2 details {house},father name is {self.father},mother name is {self.mother}")

c2=Child2("murali")
# c2.details()
c2.details1("uma")
c2.details2()
'''
#Multiple Inheritance
'''
class Parent1:
    def parent1(self,father):
        self.father=father
        print("parent1 details")

class Parent2:
    def parent2(self,mother):
        self.mother=mother
        print("Parent2 details")

class Child(Parent1,Parent2):
    def details(self):
        print(f"The child father is {self.father} and the mother is {self.mother}")


c=Child()
c.parent1("murali")
c.parent2("uma")
c.details()

'''
'''
#Hierarchical inheritance
class Parent:
    def details(self,father,mother):
        self.father=father
        self.mother=mother
class Child1(Parent):
    def child1(self):
        print(f"Child 1 father and mother is {self.father} and {self.mother}")
class Child2(Parent):
    def child2(self):
        print(f"Child2 father and mother are {self.father} and {self.mother}")


c1=Child1()
c2=Child2()
c1.details("murali","uma")
c2.details("murali","uma")
c1.child1()
c2.child2()
'''

