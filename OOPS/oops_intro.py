#its is programming approach in which ,we organize our code using classes(categories) and objects
#A car category has properties(brand ,color,model,speed)and behaviors(start,stop,accelerate,brake)
#Each car object(different car brands) under the category can have its own properties and behaviors
#In real oops programing properties are represented using attributes
#Behaviors are represented using methods(functions inside oops class)
#Objects are instance of class
#class is the blue print of object
#Terms in oops-class,objects,Attributes,methods
#Adv:1.Code reusability,2.code maintainability,3.encapsulating methods and data,4.organizing entire code scripts

#1.usage new
class CarClass:
    color="black"
    model="electric"

    def start(self):#Self refers to the current object using which we invoked the method
        print("Engine started")
    def stop(self,distance):
        self.distance=distance#Instance variable is created ,to use in other methods inside the class
        print(f"Car stopped at {distance}")
    def detail(self):
        print(f"The car started and stopped at {self.distance} kms")

car1=CarClass()#Creating objects
#print(color)#cannot be access variables inside class directly
print(car1.color)
car2=CarClass()
print(car2.color)
car1.speed="100Kmph"
print(car1.speed)
#print(car2.speed)
car1.start()
car2.start()
car1.stop(10)
#car2.stop()
car1.detail()
#In this case the value 10 is reused inside detail method ,this is possible both stop and
#detail method are invoked using the same object(car1)
car2.stop(50)
car2.detail()