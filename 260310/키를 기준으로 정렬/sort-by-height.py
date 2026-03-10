# n = int(input())
# name = []
# height = []
# weight = []

# for _ in range(n):
#     n_i, h_i, w_i = input().split()
#     name.append(n_i)
#     height.append(int(h_i))
#     weight.append(int(w_i))

# # Please write your code here.

class Student:
    def __init__(self, name, height, weight):
        self.name = name 
        self.height = height
        self.weight = weight
    
n = int(input())
student = []
for i in range(n):
    name, height, weight = input().split()
    student.append(Student(name, height, weight))

student.sort(key = lambda x : x.height)

for i in range(n):
    print(student[i].name, student[i].height, student[i].weight)