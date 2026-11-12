#1.interview question
list6=[10,20,30,40]
name="ABC"
#Expected o/p [10,20,"ABC",30,40]

list6.insert(2,"ABC")
print(list6)

#2.Create a tuple and add a new element in its second last index position
num=list(num)
num.insert(4,"appu")
num=tuple(num)
print(num)

#3.input an age from user and check whether is minor or not
age=int(input("Enter the age"))
if age>=18:
    print("The person is not minor")
else:
    print("The person is minor")

#4.input an age and nationality from the user and check whether the person is eligible for voting
age=int(input("Enter the age"))
nationality=input("Enter the nationality").lower()
if (age>=18 and nationality=="india"):
    print("Eligible for voting")
else:
    print("Not eligible for voting")


#Input a number from user and check it is even or odd

a=int(input("Enter the number"))
if a%2==0:
    print(f"{a} Even number")
else:
    print(f"{a} Not even number")

#Input a number from user and check if it is divisible by 5 or not
a=int(input("Enter the number"))
if a%5==0:
    print(f"{a} is divisible by 5")
else:
    print(f"{a} is not divisible by 5")

#Check a number is positive or not

a=int(input("Enter the number"))
if a<0:
    print(f"{a} is a negative number")
else:
    print(f"{a} is not a negative number")
#Check a number is zero or not
a=int(input("Enter the number"))
if a==0:
    print("The number is zero")
else:
    print("The number is not zero")

#input the mark ,set the pass mark and check whether pass or fail
a=int(input("Enter the mark"))
if a>=25:
    print("Passed")
else:
    print("Failed")

#Enter age and set entry fee and check eligibility for discount for senior citizen
age=int(input("Enter the age"))
fee=100
if age>=50:
    newfee=fee-(fee*10/100)
    print(f"new fee for senior citizen is {newfee}")
else:
    print(f"New fee is {fee}")