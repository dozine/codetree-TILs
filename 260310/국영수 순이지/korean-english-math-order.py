# n = int(input())
# name = []
# korean = []
# english = []
# math = []

# for _ in range(n):
#     student_info = input().split()
#     name.append(student_info[0])
#     korean.append(int(student_info[1]))
#     english.append(int(student_info[2]))
#     math.append(int(student_info[3]))

# Please write your code here.

n = int(input())



class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = []
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append(Student(name, kor, eng, math))

students.sort(key = lambda x : (-int(x.kor), -int(x.eng), -int(x.math)))

for i in range(n):
    print(students[i].name, students[i].kor, students[i].eng, students[i].math)