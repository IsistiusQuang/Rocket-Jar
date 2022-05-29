from random import choice
# class MyClass:
#     def __init__(self,mylist):
#         self.mylist = mylist

#     def main_func(self):
#         def max_func(self):
#             largest = self.mylist[0]
#             for i in self.mylist:
#                 if i > largest:
#                     largest = i
#             return largest

#         def min_func(self):
#             smallest = self.mylist[0]
#             for i in self.mylist:
#                 if i < smallest:
#                     smallest = i
#             return smallest

# myobj = MyClass([10,20,30])
# print(myobj.main_func(myobj.max_func()))

ran_list = [-2.0,-1.0,1.0,2.0]
new_ran = [i for i in ran_list if i < 0]

print(f"new_ran = {new_ran}")
print(f"ran_list = {ran_list}")
