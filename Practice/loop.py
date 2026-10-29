# for i in range(5,0,-1):
# #     print(i)
# l = 3
# for i,v in enumerate(l):
#     print(i,v)
# list = ["Bhavya","Krish","Aryan"]
# list.append("Ryan")
# list.remove("Krish")
# # print(list)
# list = ["bahvay","keish","rayn"]
# list.insert(2,"line")
# list.pop()
# list[2]="Right"
# list.remove("keish")
# print(list)
# list.sort()
# print(list)
# list.append("asper")
# res = sorted(list)
# # print(res)
# l =[
#     {"name":"Iphone","price":200000},
#     {"name":"Smasung","price":20000},
#     {"name":"MI","price":10000}
# ]
# sort = sorted(
#     l,
#     key=lambda l: l["price"]
# )
# # print(sort)
# tup = 100,"Hi",True
# print(type(tup))
# l = ([1,2],[3,4])
# l[0].append(3)
# print(l)
# l = [1,2,3,4]
# l1 = ["bhvya","kridh"]
# for i,i1 in zip(l,l1):
# #     print(i,i1)
# l=[1,2,3,4]
# even = ["even" for i in l if i%2==0]
# # print(even)
# prices = [100,40,50,80,30]
# discounted = [
#     price*0.2
#     for price in prices
#     if price >=50
# ]
# print(discounted)
num = [1,2,3,4,5]
sqr = {number:number ** 2 for number in num}
print(type(sqr))
{"u1":["login"],
 "u2":["purchase"],
 "u3":["logout"]}