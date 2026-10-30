# # # # class Employee():
# # # #     def __init__(self,first,last,pay):
# # # #         self.first=first
# # # #         self.last=last
# # # #         self.email=first + '.' + 'last' + '@company.com'
# # # #         self.pay=pay
# # # #     def full_name(self):
# # # #         return self.first + " " + self.last
# # # # emp_1= Employee('Bhavya','Mehta',75000)
# # # # emp_2= Employee('Shreyal','Shah',90000)

# # # # print(emp_1.full_name())
# # # # print(emp_2.full_name())
# # # class Employee:
# # #     No_of_emps=0
# # #     raise_amount=1.8
# # #     def __init__(self,first,last,pay):
# # #         self.first=first
# # #         self.last =last
# # #         self.pay=pay
# # #         Employee.No_of_emps+=1
# # #     def apply_raise(self):
# # #         return self.pay*self.raise_amount
# # # emp_1=Employee('Krish',"Shah",800)
# # # emp_2=Employee("Rahul",'Patel',900)
# # # print(Employee.apply_raise)
# # # print(Employee.No_of_emps)
# # # print(emp_1.apply_raise())
# # class Employee:
# #     No_of_emps=0
# #     raise_amount=1.8
# #     def __init__(self,first,last,pay):
# #         self.first=first
# #         self.last =last
# #         self.pay=pay
# #         Employee.No_of_emps+=1
# #     def apply_raise(self):
# #         return self.pay*self.raise_amount
# #     @classmethod
# #     def set_raise_amt(cls,amt):
# #         cls.raise_amount=amt
# # emp_1=Employee('Krish',"Shah",800)
# # emp_2=Employee("Rahul",'Patel',900)
# # emp_1.set_raise_amt(1.05)
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)
# class Model:
#     f='Scki-learn-every'
# model_a=Model()
# model_b=Model()
# model_a.name = "DecisionTree"
# model_b.name = "RandomForest"
# model_a.accuracy=0.95
# model_b.accuracy=0.95
# print(model_a.__dict__)
# print(model_b.__dict__)
# print(Model.__dict__)

# class MLExperiment:
#     def __init__(self,name,accuracy,training_time):
#         self.name= name
#         self.accuracy=accuracy
#         self.training_time=training_time

# experiment_a = MLExperiment("Decision Tree",0.95,5)
# experiment_b = MLExperiment("Random Forest",0.98,4)

# print(experiment_a.__dict__)
# print(experiment_b.__dict__)
# class Model:
#     def show(self):
#         print("Enginerr")

# ml = Model()
# ml.show()
# print(ml.show.__self__)
# print(ml.show.__func__)

# class Model:
#     frame = 'Scikit-learn'
#     @classmethod
#     def disPlay(cls):
#         print(cls.frame)
# # Model.disPlay()
# class MLModel:

#     framework = "Scikit-learn"

#     @classmethod
#     def change_framework(cls, name):
#         cls.framework = name


# a = MLModel()
# b = MLModel()

# a.change_framework("PyTorch")

# print(a.framework)
# print(b.framework)
# print(MLModel.framework)

# class MLExperminet:
#     organization = "AI Research Lab"
#     def __init__(self,model_name,accuracy):
#         self.model_name=model_name
#         self.accuracy=accuracy
#     @classmethod
#     def change_organization(cls,new_name):
#         cls.organization=new_name
#     @classmethod
#     def from_config(cls,config):
#         cls.config=config
# a=MLExperminet("Iphone",0.95)
# b=MLExperminet("Samsung",0.98)
# a.organization("AI Power Hub")
# print(a)
# print(b)
# print(a.organization)

class MLModel:

    framework = "Scikit-learn"

    def __init__(self, model_name, accuracy):
        self.model_name = model_name
        self.accuracy = accuracy

    @staticmethod
    def validate_accuracy(accuracy):
        return  0<=accuracy<=1
    
    def display_info(self):
        return self.model_name,self.accuracy
model_a = MLModel('Sklearn',0.90)
model_b = MLModel('pandas',0.98)
model = MLModel("Random Forest", 0.98)

print(model_a.display_info())
print(model_b.display_info())


print(MLModel.validate_accuracy(0.98))