# list1=["mango","banana","apple","banana","apple","mango","apple"]
# new_details={}
# for i in list1:
#     if i in new_details:
#         new_details[i]+=1
#     else:
#         new_details[i]=1
# print(new_details)

#employee->id,name,salary->salary,details->id,name,salary

class Employee:
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name

class Salary:
    def __init__(self,salary):
        self.salary=salary

class Details(Employee,Salary):
    def details(self):
        print(f"details are {self.emp_id} {self.name} {self.salary}")

obj=Employee(2,"varsha")
obj1=Salary(89998977867)
obj2=Details()
obj2.details()


