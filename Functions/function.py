#Functions are the block of reusable code where logic will be defined in the parent module
#Execution can be performed in any one of the child module.
#.py file extension called -module
#def function_name(always in lower key,if 2 words are there then use underscore)
#syntax for function: def function_name(): ->definition/declaration of the function
# {
#    block of codes
# }
#function_name()   ->invocation/coding of the function

#wp function to print "hello world"
'''
def message():#Non -parameterized
    print("Hello world")
#print("hi")
message()

#Type of functions->parameterized and non-parameterized

def greeting(a):#parameter list
    print(f"Hello dear {a}")

greeting("varsha")
greeting("Anandhu")

#The value passed through invocation is argument
#The variable that stores the argument is called parameter
#This together is called parameterized function

#Type of parameters/arguments:All data types can be passed as arguments
def student(name,age,place,contact):
    print(f"{name}-{age}-{place}-{contact}")
student("varsha",32,"kollam",[1234,5643])

#Default parameters
def student(name,age,place,contact,grade="5th grade"):
    print(f"{name}-{age}-{place}-{contact}-{grade}")
student("varsha",32,"kollam",[1234,5643])
student("Anandhu",34,"kollam",[321,877],"6th grade")

#Arbitary Arguments[*args]

def details(*data):
    print(data)

details("varsha",32,"kollam",[1234,5643]) #In output it will convert into a tuple

#Keyword arguments
def details(age,name):
    print(age,name)

details(name="varsha",age=32)

#Arbitary keyword arguments[**kwargs]
def details(**data):
    print(data)

details(name="varsha",age=32)
details(name="Anandhu",age=32,place="kollam")'''

#Return statements
#
# def addition(a,b):
#     #print(a*b)
#     return a+b
# print(addition(20,30))

#Scope of a variable-scope means the area of a program where the variable can be accessed or used
#There are two type of scope -1.Local scope and global scope
#Local variable=It is the variable declared inside a function , can be accessed only inside the function
# def show():
#      name="varsha"
#      print(name)
# show()
# #print(name)

#Global variable->It is declared outside all the function and can be accessed both inside and outside of the functions
# name="varsha"
# print(name)
# def show():
#      name="anandhu"
#      print(name)
# show()
# print(name)

#using global keyword you can modify the scope of a locally declared variable
name="varsha"
print(name)
def show():
     global name,x
     name="anandhu"
     print(name)
     x=20
show()
print(name)
print(x)

