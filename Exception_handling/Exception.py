'''
Error:A problem in aprogram that prevents it from working as intended
1.incorrect syntax,incorrect program logic,invalid operation
'''
# if 10>5
#     print("Hello")
#SyntaxError: expected ':' (eg:for syntax error)

# print(name)
#NameError: name 'name' is not defined(name error)

# list1=[10,20,30]
# print(list1[5])
#IndexError: list index out of range(index error)

#number=int("hello")
#ValueError: invalid literal for int() with base 10: 'hello'(value error))
#print(10/0)  ZeroDivisionError: division by zero
# dict1={"name":"varsha","age":30}
# print(dict1["location"])

#KeyError: 'location'

'''
its an error ,that occurs during a program execution and interrupts the normal flow of the program

'''
#syntax
#try:
    #code that may cause an exception
#except:
    #code to handle the exception

# else:execute when no exception occurs
# finally:execute irrespective of exception
# try:
#     num=int(input("Enter the number"))
#     result=100/num
#     print(result)
# except ValueError:
#     print("Please enter the valid integer")
#
# except ZeroDivisionError:
#     print("Please enter a non zero value")
# print("Hello")
'''
try:
    num=int(input("Enter the number"))
    result=100/num

except ValueError:
    print("Please enter the valid integer")

except ZeroDivisionError:
    print("Please enter a non zero value")
else:
    print(result)
    print("No exception occurred")
finally:
    print("Program execution completed")
'''
'''
raising exception using raise keyword-if we wnat to intentionally generate an 
intentional exception when a particular condition occurs
'''
#eg:
# age=1
# if age<18:
#     raise ValueError("Age must be 18 and above")
# print("Eligible")
#
# def withdraw(balance,amount):
#     if amount>balance:
#         raise ValueError("Insufficient balance")
#     return balance-amount
#
# print(withdraw(50,150))
# print(withdraw(50,20))

#Exception handling in playwright
'''
1.element not found
2.Locators too long to become actionable
3.browser gets closed unexpectedly
'''
'''
 def login(username, password): 
  
     try: 
         print("Opening login page...") 
  
         if username == "": 
             raise ValueError("Username cannot be empty") 
  
         if password == "": 
             raise ValueError("Password cannot be empty") 
  
         if username == "admin" and password == "admin123": 
             print("Login Successful") 
  
         else: 
             raise Exception("Invalid username or password") 
  
     except ValueError as e: 
         print("Validation Error:", e) 
  
     except Exception as e: 
         print("Login Error:", e) 
  
     else: 
         print("Login test executed successfully") 
  
     finally: 
         print("Closing browser...") 
         print("Test execution completed") 
  
  
 # Test Case 1 
 login("admin", "admin123") 
  
 print("----------------------") 
  
 # Test Case 2 
 login("admin", "wrong123") 
  
 print("----------------------") 
  
 # Test Case 3 
 login("", "admin123")

#Try the above code: exception handling including raise keyword
'''