# with open("text.txt", "r", encoding="utf-8") as file:
#     # content = file.read()
#     line = file.readline()
#     content = file.read()
# print(content)
# # print(line)
# with open('text.txt','r',encoding='utf-8') as file:
#     f = file.readlines()
# # print(f[0])
# with open('text.txt','r',encoding='utf-8') as file:
#     for line in file:
#         print(line)
#         line = line.split()

#         if line:
#             print(line)
# lines = [
#     "Training started\n",
#     "Accuracy: 0.94\n",
#     "Training completed\n",
# ]
# with open('text.txt','a',encoding='utf-8') as file:
#     X=file.writelines(lines)
# print(X)
with open('text.txt','r+',encoding='utf-8') as file:
    x=file.readlines()
    y=file.writelines('ree')
    z=file.write('wwwww')
print(x)