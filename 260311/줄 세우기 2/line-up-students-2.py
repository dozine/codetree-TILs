n = int(input())


# Please write your code here.
class Student:
    def __init__(self,i,h,w):
        self.i = i
        self.h = h
        self.w = w
students=[]
for i in range(n):
    h,w = map(int,input().split())
    students.append(Student(int(i),h,w))

students.sort(key=lambda x : (x.h, -x.w))

for student in students:
    print(student.h, student.w, student.i+1)