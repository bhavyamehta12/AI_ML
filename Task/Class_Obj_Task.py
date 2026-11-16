class StudentInfo:
    def __init__(self,student_rollno,student_name):
        self.student_rollno=student_rollno
        self.student_name=student_name
class StudentMarks:
    def __init__(self,student_rollno,student_marks_one,student_marks_two,student_marks_three):
        self.student_rollno=student_rollno
        self.student_marks_one=student_marks_one
        self.student_marks_two=student_marks_two
        self.student_marks_three=student_marks_three
class Main:
    def __init__(self,no_of_students):
        self.no_of_students=no_of_students
        self.student_record=[]
        for i in range(no_of_students):
            student_name=input("Enter Name Of Student: ")
            roll_no=int(input(f"Enter Roll No Of {student_name}: "))
            obj_info = StudentInfo(roll_no,student_name)
            marks1=int(input("Enter Marks for Subject 1: "))
            marks2=int(input("Enter Marks for Subject 2: "))
            marks3=int(input("Enter Marks for Subject 3: "))
            obj_marks = StudentMarks(roll_no,marks1,marks2,marks3)
            self.student_record.append((obj_info,obj_marks))



        


