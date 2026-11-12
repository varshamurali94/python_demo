#wpp to iterate/print "hello world 10 times
#syntax-> for item in iterable
#Iterable-> string,list,tuple,set,dictionary,range of numbers
'''
#RANGE ITERATION
for i in range(10):#(0,1,2...10)
    print(i,"- Hello world")

#wpp to iterate first 10 natural numbers
#Syntax for range -> (starting index,ending index+1,step)
for i in range(1,11):
    print(i)
#wpp to iterate numbers from 15-35
for i in range(15,36):
    print(i)

#wpp to iterate first 10 natural numbers and print all even numbers?
#method 1
for i in range(1,11):
    if i%2==0:
        print(i)
#method 2

for i in range(2,11,2):
    print(i)

#wpp to iterate first 10 natural numbers and get even and odd numbers in seperate list

evenlist=[]
oddlist=[]
for i in range(1,11):
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print(f"Even list is {evenlist}")
print(f"odd list is {oddlist}")

#wpp first 10 natural numbers and get the square of all the numbers in seperate list

squarelist=[]
for i in range(1,11):
    squarelist.append(i*i)
print(squarelist)

#wpp first 10 natural numbers and get the sum of squares
sum=0
for i in range(1,11):
    sum+=i*i
print(f"sum is {sum}")

#get the sum of first 20 natural numbers
sum=0
for i in range(1,21):
    sum+=i
print(sum)

#get the product of first 10 natural numbers
product=1
for i in range(1,11):
    product*=i
print(product)

#get the sum of cubes of first 5 natural numbers
sum=0
for i in range(1,6):
    sum+=i*i*i
print(sum)
#get the sum of cubes of first 10 even numbers
sum=0
for i in range(1,11):
    if i%2==0:
        sum+=i*i*i
print(sum)

#LIST ITERATION
list1=[1,2,3,4]
for i in list1:
    print(i)

#TUPLE ITERATION
tup1=(20,5,"varsha",7,"True")
for i in tup1:
    print(i,end="  ")#'end' is used to make into a single line

#STRING ITERATION
#s="hello"
s="hello-good-morning"
print(s.split("-"))
for i in s.split():#split will convert the sentences into words where spaces are coming and converted into a list
    print(i)

#DICTIONARY ITERATION
dict1={"name":"varsha","age":32}
for key,value in dict1.items():
    print(key,value)

#SET ITERATION ->usually we won't do it
set1={1,5,7,"VARSHA"}
for i in set1:
    print(i)'''




