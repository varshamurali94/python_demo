#Encapsulation is the process of combining data(variable) and methods into a single unit
#called a class .While controlling access to the data
#Python has 3 common access level/Access modifiers
#1.Public:(eg:name="varsha"),can be accessed normally
#Protected:(eg:_name="varsha")intended for internal and subclass uses
#Private:(eg:__name="varsha")can be accessed using base class objects

#examples for private variable-password
#Example for private method-balance enquiry using ATM card

class Employee():
    def __init__(self,name,salary,password):
        self.name=name#public variable
        self._salary=salary#protected variable
        self.__password=password#Private variable
    def display_name(self):
        print(f"Employee name is {self.name}")
    def _display_salary(self):
        print(f"Empoyee salary is {self._salary}")
    def __display_password(self):
        print(f"Employee password is {self.__password}")
    def show_details(self):
        self.__display_password()

obj=Employee("Varsha",40000,"abc123")
#Accessing public variable and method
obj.display_name()
print(obj.name)
#Accessing protected variable and method
obj._display_salary()
print(obj._salary)
#Accessing private variable and method
##print(obj.__password)
#obj.__display_password()#Cannot access private method and variables directly
obj.show_details()

#Getter and setter method:
#Getter Method:Method used to retrieve the value of a private variable
#Setter method:is used to modify the value of a private variable usually with validation


