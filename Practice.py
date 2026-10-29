# y = [2, 4, 6, 8, 10]
# x=list(map(lambda x:x**2,y))
# print(x)
# u= [x**2 for x in y]
# print(u)
# f=[]
# for i in y:
#     f.append(i**2)
# print(f)
y = [12, 7, 18, 5, 20, 9, 14, 3]
x=list(filter(lambda x:x%2==0,y))
print(x)
z=[]
for i in y:
    if i%2==0:
        z.append(i)
print(z)
f=[x for x in y if x%2==0]
print(f)