#Mutable Datatypes-list,set,dictionary
#Immutable Datatypes-Integer,Float,Boolean,String,Tuple
#Keywords-Reserved meaningful words in python, cannot be provided as a variable name

# import keyword
# print(keyword.kwlist)#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# #Difference between keyword,identifier and variable
#
# #variable declaration can be performed to store or assign values
# #variable declaration eg:
# x=10
# X=20
# abcAB=30
# abc_=40
# _abc=59
# ab_c=76
# _=50
# abc123=76
# a12_c=76
# #12abc=76 cannot start with a digit, spaces are not allowed
# #Must start with a letter or underscore
# #/vsddf=675#special characters are not allowed
#
# #Identifier->Are variables which are meaningful in nature
# name="varsha"
# age=31
# price=4.6
#
# #Case sensitivity in python
# #unicode represents a characters individual code of representation in normal english
# x=10
# X=30
# print(X)
#
#
# a="Python"
# b="python"
# print(a==b)#It will check both case an value and returns a boolean response
#
# #String methods
#
# str1="varshaABC is a student"
# print(str1.upper())
# print(f"The original string is {str1}")
# x=str1.lower()
# print(x)
# print(str1.capitalize())#first letter of first word  get capital
# print(str1.title())#First letter of all words get capitalize
# print(str1.swapcase())#swap the case
# print(str1.find("is"))#It will give the first position of the substring
# print(str1.index("is"))
# print(str1.count("a"))
# print(str1.isupper())#To check whether the string is upper or not
# print(str1.isdigit())#To check whether the string is digit or not

#List methods

list1=[1,5,"varsha",True]
list1.append("anandhu")#To add new element at the last
list1.pop()#To remove the last element from the list
print(list1)
list2=[1,6,"varsha"]
list1.extend(list2)#To add elements from list1 to list2
print(list1)
list1.insert(0,"malu")
print(list1)
list1.append(6)
list1.remove(6)#Removes the first occurance of the element
print(list1)
print(list1.count("varsha"))
#list1.clear()#It will clear the content of the list
print(list1)
list1.reverse()
print(list1)
list3=list1.copy()
print(list3)
list4=[5,8,2,1,2.5,0]
list4.sort(reverse=True)#sort only used to convert to ascending order and if we give reverse=True it will convert to opposite(descending order)
print(list4)
list5=["book","pen","Z","K","d","BOOK","PEN","Apple","aPPLE","appLE","applE"]
list5.sort()#Convert to alphabetical order first preference for uppercase it is applicable to same type(eg:only number or only letter)
print(list5)
#Methods->append,pop,insert,extend,clear,copy,sort,reverse,remove

#Build in methods in python list
num=[5,1,7.8,0,3]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
#interview question
list6=[10,20,30,40]
name="ABC"
#Expected o/p [10,20,"ABC",30,40]

list6.insert(2,"ABC")
print(list6)
#-----------------------------------------

#Tuple Methods
num=(2,7.6,1,2,9)
print(num.count(2))
print(num.index(7.6))
#Create a tuple and add a new element in its second last index position
num=list(num)
num.insert(-1,"appu")
num=tuple(num)
print(num)

#Packing and unpacking of tuple
student=("varsha",32,"female","kollam","TVM") #This is packed version of tuple
name,age,gender,*place=student#This is unpacking,last more value goes to the last variable which has * (also called arbitary argument making)
print(age,name,gender)
print(place)

tuple7=("a","b","c","d","e","g")
x,*y,z,q=tuple7
print(x,z,q)
print(y)

#Dictionary methods

dict1={"name":"varsha","age":32,"gender":"Female"}
print(dict1["age"])
dict1["Location"]="kollam"
print(dict1)
print(dict1.get("name"))
dict1.update({"age":30})
print(dict1)
dict1["age"]=25
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#Each key-value pair in a dict is called items







