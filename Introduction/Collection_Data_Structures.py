#COLLECTION DATATYPES-DATASTRUCTURES-can store multiple values in a single variable
#Tuple,List,Set,Dictionary

#LIST
x=list()
print(x)
x=[1,1.3,True,"varsha",1,1,"varsha"]
print(x)
#List features->1.Ordered,2.Duplication allowed,3.Mutable,Multiple datatype can add, indexing,slicing
print(x[4])

#SLICING
print(x[0:3])
y=x[2:7]
print(y)

len_x=len(x)#index of last element=len_x-1
print(x[len_x-1])
print(len_x)

print(x[0:])
print(x[:7])
print(x[:])
print(x[0:7:2])
#slicing syntax:Starting index:ending index+1:step
#negative indexing->negative index starts from right side(-1)
x=[1,1.3,True,"varsha",1,1,"varsha"]
print(x[-3])
print(x[-5:-1])#collect the elements in indexes -5,-4,-3, slicing always starts from small to large

#Tuple->it is the immutable collection data structure in python
x=tuple()
x=()
print(x)
print(type(x))
x=(10,10.5,"varsha",True,True,10,[1,5,8,"varsha"],(2,7,5,"anandhu"))
print(x)
# Tuple features:indexing,ordered,duplication allowed,slicing,multidata storage,immutable
# Tuple is faster than list in case of large number of data as it is immutable

#Set Features-> Unordered,no duplication,no indexing, no slicing,mutable,cannot add list/tuples
x=set()
print(x)
print(type(x))
x={2,4}#empty curly braces denote dictionary ,at lease 1 value required to make it a set
print(type(x))
x={2,4.4,"varsha",True,2}
print(x)

#Dictionary Feature->The only named index data structure in python
x=dict()
print(x)
print(type(x))
x={"name":"varsha","age":31,"gender":"Female","name":"anandhu","Contact":[1234,5678]}
print(x)
print(x.values())
print(x.keys())
print(x["age"])
print(x.items())
print(x["Contact"][0])