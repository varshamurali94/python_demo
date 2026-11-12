#Write a function to count the vowels in s string
'''
word=input("Enter the word")
vowel_list=[]
count=0
for i in word:
    if i in "aeiouAEIOU":
        vowel_list.append(i)
        count+=1
print(f"The count of vowel in the string is {count} and the vowels are {vowel_list}")
print()
'''

#write a function to check whether a test case is passed or fail
'''
output_text1="12 tests passed"
output_text2="10 pass 2 Failed"

def check_test_status(status):
    if "Failed" in status:
        print("Testcase is Failed please try again")
    else:
        print("Test case is passed")

check_test_status(output_text1)
check_test_status(output_text2)
'''
#write a function to check whether a username is valid (length more than 5)
'''
user_name=input("Enter the username")
def user_check(check):
    if len(user_name)>5:
        print(f"The username: {user_name} is valid ")
    else:
        print(f"The username: {user_name} is not valid")

user_check(user_name)
'''
#Create a function to validate an email address(Can include characters,digit,.,com/in,gamil,@ starts with char
#method1
'''

emai_address=input("Enter the email address")
def email_check(email):
    first_char=emai_address[0]
    #print(type(first_char))
    if "@" in email and "gamil" in email or ".in" in email or ".com" in email:
        print(f" {emai_address} is valid")
    else:
        print(f"{emai_address} is not valid")
email_check(emai_address)
'''
#method2-->need to check agin by th tuitor
'''
emai_address=input("Enter the email address")
def email_check(email):
    first_char=email[0]
    char4=(type(first_char))
    print(char4.isdigit())
    if (not first_char.isdigit()) and "@" in email and "gamil" in email or ".in" in email or ".com" in email:
        print(f" {emai_address} is valid")
    else:
        print(f"{emai_address} is not valid")
email_check(emai_address)
'''
#create a function to convert a browser name into lowercase

browser_name=input("Enter the browser name")
def check_browser(browser):
    print(browser.lower())

check_browser(browser_name)

#In keys of strict check , always use "=="(both value and case are equal)
#In case of return statement ,check all conditions are fulfilled in prior
#after return statement one function automatically stop the execution
#Always use return statement when we want to store the o/p
#diff b/w print and return : print:execution will continue even after print
#whereas , execution stops after return

