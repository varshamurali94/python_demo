
# Polymorphism means one name with many forms .It will allow same method name(function)
# or operator to behave differently depending on the obj\
# The build it polymorphic operator in python is '+'(for numbers it will perform addition
# and for string it will perform concatenation)


class Parent:
    def skill(self):
        print("Teaching skill")
class Child1(Parent):
    def skill(self):
        super().skill()
        print("Singing")
class Child2(Parent):
    def skill(self):
        print("Dancing")

c=Child1()
#c.skill()
c2.Child2()
c2.skill()

#in python the type of polymorphism its supports is method overridding
