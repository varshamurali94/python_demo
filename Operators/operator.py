#Arithmetic Operators->+,-,*,%,/,**,//
a,b=10,20
print(a+b)#30
print(a-b)#-10
print(a*b)#200
print(a/b)#.5
print(a//b)#0(Floor devision without decimel
print(a%b)#0Reminder
print(a**2)#100

a,b="hello","varsha"
print(a+b)#concatenation
a,b="hello",10
#print(a+b)#can only concatenate str (not "int") to str
a,b=10,"hello"
#print(a+b)#unsupported operand type(s) for +: 'int' and 'str'

#Comparison Operators-> >,<,>=,<+,!=,=,== (Returns boolean value)
a,b=20,"20"
#print(a>b)
#print(a<b)
print(a==b)#It will check both value and datatype
#print(a=b)#value assignment
print(a!=b)

#Assignment Operators->
a,b=10,20
#a=a+b
a+=b#a-=b , a*=b it is possible for all arithmetic operators
print(a)

#Logical operators -> and ,or,not
a,b,c=10,20,30
print(a<b and b<c and c>a)#Returns True if all conditions are true
print(a<b or b>c or c>a)#If any one of the condition is true, returns true
print(not(a>b))#Usually we will only one condition for this,to handle the reverse case

#Membership operators-> in ,not in
a="hello"
print("o" in a)
list1=[10,20,30]
print(50 not in list1)
dict1={"name":"varsha","age":32}
print("name" not in dict1)

#Identity Operators -> is ,is not(Equal as ==,!=)
a,b=10,20
print(a is b)
print(a is not b)

