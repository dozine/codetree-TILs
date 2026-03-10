# 클래스 선언
class Student:
    def __init__(self, height, weight, number):
        self.height, self.weight, self.number = height, weight, number


# 변수 선언 및 입력
n = int(input())
students = []
for i in range(1, n + 1):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight, i))

# Custom Comparator를 활용한 정렬
students.sort(key=lambda x: (-x.height, -x.weight, x.number))

# 출력
for student in students:
    print(student.height, student.weight, student.number)
