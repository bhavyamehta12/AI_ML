from functools import reduce

ls = int(input("Enter No of Lists : "))
lists=[]
y=[]
for i in range(ls):
    n = int(input(f"Enter number of elements for list {i + 1}: "))
    elements = list(map(int,input(f"Enter {n} elements for list {i + 1}, separated by spaces: ").split()))
    lists.append(elements)  
for i, ls in enumerate(lists, start=1):
    print(f"ls{i} = {ls}")
for i in lists:
    y+=i
print(y)
print("Maximun No :",max(y))
print("Minimun No :",min(y))
s = reduce(lambda a,b:a+b,y,0)
print("Sum is :",s)
result = list(map(lambda x: x**2, y))
print("Square is :",result)
