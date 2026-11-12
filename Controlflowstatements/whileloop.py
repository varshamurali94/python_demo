#WPP to iterate first 10 natural numbers
# for i in range(1,11):
#     print(i)
#using while loop
'''
i=1
while(i<=10):
    print(i)
    i+=1
#iterate numbers 20-40

i=20
while(i<=40):
    print(i)
    i+=1

#iterate first 10 natural numbers in reverse order
i=10
while(i>=1):
    print(i)
    i-=1'''
#A for loop is generally used when we want to iterate over a sequence or repeat a known num of times.
#eg:iterate 1-5
#A while loop is used when we want to repeat a block of code as long as the condition is True
#Eg:To login with valid credentials , ATM cash withdrawal using pin

#Interview Qes:wpp to find the factorial of a number
#eg:for the number 5,factorial =5*4*3*2*1=120
#using while loop
'''
num=int(input("Enter the number"))
i=num
fact=1
while(i>=1):
    fact*=i
    i-=1
print(f"Factorial of {num} is {fact}")

#Using for loop
num=int(input("Enter the number"))
fact=1
for i in range(1,num+1):
    fact*=i
    #i+=1
print(f"factorial is {fact}")

#vvvi ques wpp that repeatedly ask the user to enter a username and password until both correct
username="admin"
password="admin123"
user1=""
pass1=""
while(user1!=username and pass1!=password):
    user1=input("Enter username")
    pass1=input("Enter password")
    if(user1!=username or pass1!=password):
        print("Try again")

print("Login successful")'''

#ATM pin verification -provide a valid pin num , receive pin from users and check the validity

pin=123
pin1=""
while(pin1!=pin):
    pin1=int(input("Enter the valid pin"))
    if(pin1!=pin):
        print("Try again")
print("PIN is valid")





