# class Parent:
#     net_worth="100cr"
#     def skill(self):
#         print("Teaching skill")
# class Child(Parent):
#     def skill2(self,job):
#         print(f"Child job is {job}")
#
# c=Child()
# c.skill2("Engineer")
# c.skill()
# print(c.net_worth)

#
# class Parent:
#     def __init__(self,net_worth):
#         self.net_worth=net_worth
#        # net_worth="100cr"
#     def skill(self):
#         print("Teaching skill")
# class Child(Parent):
#     def __init__(self,net_worth):
#         super().__init__(net_worth)
#     def skill2(self,job):
#         print(f"Child job is {job} and networth is {self.net_worth}")
#
# c=Child("10cr")
# c.skill2("Engineer")
# c.skill()
# print(c.net_worth)