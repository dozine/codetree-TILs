class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
student=[]

for _ in range(5):
    name, score = tuple(input().split())
    student.append(Student(name,int(score)))

min_idx=0
for i in range(1,5):
    if student[min_idx].score > student[i].score:
        min_idx=i
    
print(student[min_idx].name, student[min_idx].score)