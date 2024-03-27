class Student:
    def __init__(self,name,kor,eng,mat):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat
    
n=int(input())
students=[]
for _ in range(n):
    name,kor,eng,mat=tuple(input().split())
    students.append(Student(name,int(kor),int(eng),int(mat)))

students.sort(key=lambda x: (-x.kor,-x.eng,-x.mat))

for student in students:
    print(student.name, student.kor, student.eng, student.mat)