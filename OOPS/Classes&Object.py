# # class Employee():
# #     def __init__(self,first,last,pay):
# #         self.first=first
# #         self.last=last
# #         self.email=first + '.' + 'last' + '@company.com'
# #         self.pay=pay
# #     def full_name(self):
# #         return self.first + " " + self.last
# # emp_1= Employee('Bhavya','Mehta',75000)
# # emp_2= Employee('Shreyal','Shah',90000)

# # print(emp_1.full_name())
# # print(emp_2.full_name())
# class Employee:
#     No_of_emps=0
#     raise_amount=1.8
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last =last
#         self.pay=pay
#         Employee.No_of_emps+=1
#     def apply_raise(self):
#         return self.pay*self.raise_amount
# emp_1=Employee('Krish',"Shah",800)
# emp_2=Employee("Rahul",'Patel',900)
# print(Employee.apply_raise)
# print(Employee.No_of_emps)
# print(emp_1.apply_raise())
class Employee:
    No_of_emps=0
    raise_amount=1.8
    def __init__(self,first,last,pay):
        self.first=first
        self.last =last
        self.pay=pay
        Employee.No_of_emps+=1
    def apply_raise(self):
        return self.pay*self.raise_amount
    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amount=amt
emp_1=Employee('Krish',"Shah",800)
emp_2=Employee("Rahul",'Patel',900)
emp_1.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)