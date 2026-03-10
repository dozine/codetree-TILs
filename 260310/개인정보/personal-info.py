# 클래스 선언
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight


# 변수 선언 및 입력
students = []
for _ in range(5):
    name, height, weight = tuple(input().split())
    students.append(Student(name, int(height), float(weight)))

# Custom Comparator를 활용한 정렬 (이름순으로 정렬)
students.sort(key=lambda x: x.name)

print("name")
# 이름순으로 정렬한 결과 출력
for student in students:
    print(student.name, student.height, student.weight)

print()

# Custom Comparator를 활용한 정렬 (키순으로 정렬)
students.sort(key=lambda x: -x.height)

print("height")
# 키순으로 정렬한 결과 출력
for student in students:
    print(student.name, student.height, student.weight)
