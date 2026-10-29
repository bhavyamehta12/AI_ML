# n= int(input("Enter No of Students : "))
# students =[
#     (input("Roll_NO: "),input("Name: "))
#     for _ in range(n)
# ]
# with open('studentInfo.txt','w',encoding='utf-8') as f:
#     f.writelines(
#         map(lambda x:f"{x[0]}-{x[1]}\n" ,students)
#     )
# marks = [
#     (roll,
#     input(f"Subject 1 marks for {name}: "),
#     input(f"Subject 2 marks for {name}: "),
#     input(f"Subject 3 marks for {name}: "))
#     for roll,name in students
# ]
# with open('studentMarks.txt','w',encoding='utf-8') as f:
#     f.writelines(
#         map(lambda m:f"{m[0]}-{m[1]}-{m[2]}-{m[3]}\n" ,marks)
#     )
with open("studentMarks.txt", "r",encoding='utf-8') as f:
    averages = [
        (parts[0], sum(map(float, parts[1:])) / len(parts[1:]))
        for parts in map(lambda line: line.strip().split("-"), f)
        if parts[0]
    ]

for roll, avg in averages:
    print(f"Roll No: {roll}, Average: {avg:.2f}")
with open("studentInfo.txt", "r", encoding="utf-8") as f:
    names = {
        parts[0]: parts[1].strip()
        for parts in map(lambda line: line.strip().split("-", 1), f)
        if len(parts) == 2
    }
print(names)
with open("Agrade.txt", "w", encoding="utf-8") as f:
    records = [
        f"{roll}-{names.get(roll, 'UNKNOWN')}-{avg:.2f}\n"
        for roll, avg in averages
    ]

    f.writelines(records)