import json
#python provides a build in module called json to work with json data
# with open("file.json","r")as file1:
#     data=json.load(file1)
#     print(data)
#     print(data["name"])
'''
#json.dump()-write python data into a json file
json.dumps()-convert python data into json string
json.loads()-convert json string into python data
'''
student={"mark":43,"location":"kollam"}
with open("file.json","w") as file1:
    json.dump(student,file1)
