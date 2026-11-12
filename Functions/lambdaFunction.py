#Lambda function->it is a small anonymous funct written mostly as a single
#expression using lambda keyword
#Unlike a normal function created using def keyword , a lambda keyword does not require a function name
#or an explicit return statement

#syntax
#lambda parameters:expression
#expression operation is performed and automatically returned as a result
#wpp to add two numbers

# def addition(a,b):
#     return(a+b)
# print(addition(2,4))

#USING LAMBDA FUNCTION

# sum=lambda a,b:a+b
# print(sum(2,4))

#write a lambda function to find the square of the number

# square=lambda a:a*a
# print(square(6))

#check a number is even or odd
#
# number=lambda a:"even" if a%2==0 else "odd"
# print(number(6))
#
# #Non-paramerized lambda function
#
# greet=lambda :"Good morning"
# print(greet())

#String based question
#check the given character is a vowel or not(i/p->x="A")
# x=input("Enter the character")
# if x in "aeiouAEIOU":
#     print(f"{x} is a vowel")
# else:
#     print(f"{x} is not vowel")

#check the given character is a consonant or vowel(i/p->x="A")
# x=input("Enter the character")
# if x in "aeiouAEIOU":
#      print(f"{x} is a vowel")
# else:
#      print(f"{x} is a consonant")

#Count the number of vowels in a user input(i/p -<x="python")
# x=input("Enter the word")
# count=0
# for i in x:
#     if i in "aeiouAEIOU":
#         count+=1
#
# print(f"Number of vowel in the word is {count}")

#Count the number of vowels in a user input("python is easy to learn)
# x=input("Enter the sentance").split()
# print(x)
# count=0
# for i in x:
#     for j in i:
#        if j in "aeiouAEIOU":
#           count+=1
# print(f"Total number of vowel is {count}")

#Loop questions
#get the count of multiples of 5 from the given list

# x=[1,5,10,15,8,4]
# count=0
# for i in x:
#     if i%5==0:
#         count+=1
# print(f"multiple of 5 is {count}")

#vviIdentify the most repeated elements in the given list[5,10,5,10,5,3,2]
# x=[5,10,5,10,5,3,2]
# duplicate={}
# for i in x:
#     if i in duplicate:
#         duplicate[i]+=1
#     else:
#         duplicate[i]=1
#
# print(duplicate)
# max_count=max(duplicate.values())
# for i,j in duplicate.items():
#     if j==max_count:
#         print(f"The most repeated element is {i} and the count is {j}")

#vvi count the number of strings from the below list[5,10,"A","python","hello",3.5,False]
# list1=[5,10,"A","python","hello",3.5,False]
# count=0
# for i in list1:
#     if type(i) == str:
#         count+=1
# print(f"count of string is{count}")

