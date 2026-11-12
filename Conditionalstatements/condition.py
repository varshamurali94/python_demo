#if,elif,else
'''
#input an age from user and check whether is minor or not
age=int(input("Enter the age"))
if age>=18:
    print("The person is not minor")
else:
    print("The person is minor")
#input an age and nationality from the user and check whether the person is eligible for voting
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

#input a number and check positive,negative or zero
num1=int(input("Enter the number"))
if num1==0:
    print("The number is zero")
elif num1>=0:
    print("The number is positive")
else:
    print("The number is negative")

#Input 3 numbers and check which one is greater?
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if num1>num2 and num1>num3:
    print(f"{num1} is greater among the 3 numbers")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater among the 3 numbers")
elif num3>num1 and num3>num2:
    print(f"{num3} is greater among the 3 numbers")

#input mark from user
#>=90 grade a
#>=80 grade b
#>=70 grade c
#>=60 grade d
#<60 grade fail
#<0 or >100 invalid mark

mark=int(input("Enter mark"))
if(mark<0 or mark>100):
    print("Invalid mark")
elif(mark>=90):
    print("Grade is a")
elif(mark>=80):
    print("Grade is b")
elif(mark>=70):
    print("Grade is c")
elif(mark>=60):
    print("Grade is d")
elif(mark<60):
    print("Failed")'''

