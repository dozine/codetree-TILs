n = int(input())

class Point:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

    # self를 추가하여 인스턴스 메서드로 만듭니다.
    def get_distance(self):
        # 여기서는 절대값의 합(Manhattan distance)을 예시로 들었습니다.
        # 문제 조건이 단순히 x + y라면 self.x + self.y로 쓰시면 됩니다.
        return abs(self.x) + abs(self.y)

points = []
for i in range(n):
    x, y = map(int, input().split()) 
    points.append(Point(int(i+1), x, y))

# lambda에서 메서드를 호출할 때는 괄호()를 잊지 마세요!
points.sort(key=lambda p: (p.get_distance(), p.num))

for p in points:
    print(p.num)