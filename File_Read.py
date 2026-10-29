
# # with open('sensor.txt','w',encoding='utf-8') as file:
# #     x = file.write('''Sensor ID: S101
# # Temperature: 27.5
# # Status: Normal''')
# # print(x)
# # with open('sensor.txt','r',encoding='utf-8') as file:
# #     y=file.read()
# # print(y)
# # with open('sensor.txt','a',encoding='utf-8') as file:
# #     x = file.write('\nSensor ID: S102\n Temperature: 41.2\n Status: Warning')
# # with open('sensor.txt', 'r', encoding='utf-8') as file:
# #     for i, content in enumerate(file, start=1):
# #         print(f"Line {i}: {content.rstrip('\n')}")
# count=0
# # with open('sensor.txt','r',encoding='utf-8') as file:
# #     x=file.read()
# #     print(x.split())
# #     for i in x.split():
# #         if i=='Warning':
# #             print('Warning found: Status: Warning')
# #             count+=1
# # # print(count)
# # with open('sensor.txt','r',encoding='utf-8') as file:
# #     for line in file:
# #         if 'Warning' in line:
# #             print('Warning found: Status: Warning')
# #             count+=1
# # print(count)
# with open('sensor.txt','r',encoding='utf-8') as file:
#     print(file.tell())
#     print(file.seek(3))
#     print(file.read())
with open('sensor.txt','r',encoding='utf-8') as file:
    print(file.tell())
    x=file.readline()
    print(x)
    checkpoint = file.tell()
    print(checkpoint)
    print(file.readline())
    print(file.readline())
    print(file.tell())
    print(file.seek(checkpoint))
    print(file.readline())