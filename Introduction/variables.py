print("hello")
x=10#variable(x) is container , here 10 store in a memory in RAM and x is the reference variable of that memory address
# print(x)
# variable x is declared and value 10 is assigned /initialized
# <module> is the .py file which we created
x=20
print(x) #declaration alone cannot be performed and while re-initializing first value get removed
print(type(x)) #type checking using type() method

# BASIC DATATYPES in python-intiger,boolean,float,string(basic data types can store only one value at a time)
y=20
print(type(y))

y=True
print(type(y))

y=20.5
print(type(y))

y="varsha-/6756 #"
print(type(y))

#interview question:how data types are mentioning -->  <class 'str'>

#COLLECTION DATATYPES-DATASTRUCTURES-can store multiple values in a single variable
#Tuple,List,Set,Dictionary
#LIST
x=list()
print(x)
x=[1,1.3,True,"varsha",1,1,"varsha"]
print(x)
#List features->1.Ordered,2.Duplication allowed,3.Mutable,Multiple datatype can add, indexing,slicing
print(x[4])

