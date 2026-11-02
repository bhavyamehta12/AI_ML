# class Animal():
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     pass
# my_dog= Dog()
# # my_dog.eat()
# class animal():
#     def __init__(self,animal):
#         self.animal=animal
#     def eat(self):  
#         print(self.accuracy,"is Eating")
# class dog(animal):
#     def name(super,name):
# #         animal.eat(name)
# class MLModel:
#     framework= 'cikit-learn'
#     def train(self):
#         print("Trainin Ml Model")
#     @classmethod
#     def eat(cls):
#             print("Eating")
# class DecisionTree(MLModel):
#     def predict(self):
#         print("Makin Predictions")
# model = DecisionTree()
# model.train()
# DecisionTree.eat()
# print(model.framework)

# class animal():
#     def __init__(self):
#         self.accuracy=98
#         self.__framework=0.8
# class dog(animal):
#     def __init__(self):
#         super().__init__()
#         self.eat="eating"
# model= dog()
# print(model.accuracy)
# print(model._animal__framework)
# print(model.eat)

# Multiple Inheritance
class ParentA():
    def a(self):
        print("A method")
class ParentB():
    def b():
        print("B method")
class child(ParentA,ParentB):
    pass
model = child()
model.a()