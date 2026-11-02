# # class MLModel:
# #     def __init__(self,accuracy):
# #         self.__accuracy = accuracy
# #     def x(self):
# #         self.__accuracy+=1

# # model = MLModel(5)
# # model.x()
# # model._MLModel__accuracy=90
# # print(model._MLModel__accuracy)
# # class model:
# #     def __init__(self):
# #         self.learning=4
# # m=model()
# # m.learning=9
# # # print(m.learning)
# # class Neural:
# #     def __init__(self):
# #         self.__learning=0.1
# #     @property
# #     def learning(self):
# #         return self.__learning
# #     @learning.setter
# #     def learning(self,value):
# #         if value>0:
# #             self.__learning=value
# #         else :
# #             raise ValueError("Invalid")
# # model = Neural()
# # print(model.learning)
# # model.learning=-9
# # print(model.learning)
# class Model:
#     def __init__(self):
#         self.__learning_rate=0.01
#     @property
#     def learning_rate(self):
#         return self.__learning_rate
#     @learning_rate.setter
#     def learning_rate(self,new):
#         if self.learning_rate>0:
#             self.learning_rate=new
#         else:
#             raise ValueError("Invlid")
