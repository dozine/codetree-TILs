class Student:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
students=[]
n=int(input())
for _ in range(n):
    name,height,weight=tuple(input().split())
    students.append(Student(name,int(height),int(weight)))

students.sort(key = lambda x: (x.height, -x.weight))

for student in students:
    print(student.name, student.height, student.weight)