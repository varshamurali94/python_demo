#WPP to check whether a number is prime or not
#prime numbers-2,3,5,7,...(Those num are divisible by 1 and same numbers only)
#consider 7(device using 2,3,4,5,6)if the reminder is zero in any case the number is not prime
'''
n=int(input("Enter the number"))
if n<2:
    print("The number is not in prime number range")
else:
    for i in range(2,n):
        if n%i==0:
            print(f"The number {n} is not a prime number")
            break
    else:
        print(f"The number {n} is a prime number")
#Find the prime number in a range 10-30
prime=[]
for i in range(10,31):
    if i<2:
        print("Not in prime range")
    else:
        for j in range(2,i):
           if i%j==0:
             break
        else:
           prime.append(i)
print(prime)

#Find the count of prime number in a range 10-30
prime=[]
count=0
for i in range(10,31):
    if i<2:
        print("Not in prime range")
    else:
        for j in range(2,i):
           if i%j==0:
             break
        else:
           prime.append(i)
           count+=1
print(prime)
print(count)'''

#input a number from user and reverse it
#input=541, o/p=145
#
# num=int(input("Enter the number"))
# reverse=0
# while(num>0):
#     digit=num%10
#     reverse=reverse*10+digit
#     num//=10
# print(reverse)
#in first iteration n=541,digit=1,reverse=1(0*10+1),further n=54
#in 2nd iteration n=54,digit 4,reverse=14,n=5
#in 3rd iteration n=5,digit=5,reverse=145,n=0
#in 4th iteration condition falls and loop break

#Input a number from user and find the sum of digits of a number
#input :541 output:5+4+1
# num=int(input("Enter the number"))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num//=10
#
# print(f"sum of the number is {sum}")

#Input a string from the user and remove all the duplicate characters
#Input :"Programming" output :"progamin".Hoe many charector available in the output
'''
word=input("Enter the word")
dupli=""

for i in word:
    if i in dupli:
        continue
    else:
        dupli+=i
print(f"The final string is {dupli}")
length=len(dupli)
print(f"The number of char is {length}")
'''
#Input two numbers from user and swap it
#a,b=10,20   o/p:a,b=20,10
'''
a=int(input("First number a"))
b=int(input("Second number b"))
a,b=b,a
print(f"Swaped numbers value a and b are  {a,b}")'''

#Doubt-Find the largest number in alist without using index position
#x=[2,5,1,4,4,7,8,9,1]
'''
x=[2,5,1,4,4,7,8,9,1,-1]
largest_number=max(x)
print(f"Larget number is {largest_number}")
'''

#Doubt-identify the most repeated element in the given list [5,5,7,1,3,8,9,4]
'''
x=[5,5,7,1,3,8,9,4]
dupli={}
max_count=0
for i in x:
    if i in dupli:
        dupli[i]+=1
    else:
        dupli[i]=1
most_freq=None
for i,j in dupli.items():
    if j>max_count:
        max_count=j
        most_freq=i

print(most_freq)

'''






















