'''
In file handling ,for testing purpose the most commonly used files are txt,
json and excel
'''

#txtfile:
#Using built-in open() function
#Opening file in read mode

# file=open("data.txt","r")
# content=file.read()
# print(content)

# file1=open("data.txt","r")
# content=file1.readlines()
# print(content)

# file3=open("data.txt","r")
# content=file3.readline()
# print(content)

#Opening files in write mode

# file=open("data.txt","w")
# file.write("Hello")

file=open("data1.txt","w")
file.write("name:anandhu")

#Opening files in append mode
# file2=open("data.txt","a") #Append method id preferable
# file2.write("Contact:5432765 \n")
# file2.close()
# print(file2.closed)


#Methods applicable in existing file:read,write,append,create(x)
#Methods applicable in non-existing file:write,append,create(x)

#File handling using 'with'statement
'''
with statement automatically closed the file when the block finishes even-if  an exception
occurs
'''
# with open("data.txt","r") as file1:
#     content=file1.read()
#     print(content)
#     print(file1.closed)
# print(file1.closed)