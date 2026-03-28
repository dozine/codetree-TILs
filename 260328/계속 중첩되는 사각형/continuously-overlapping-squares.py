MAX_R = 200
OFFSET = 100

# 변수 선언 및 입력
n = int(input())
checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

x1, y1, x2, y2 = [], [], [], []
for i in range(n):
    _x1, _y1, _x2, _y2 = tuple(map(int, input().split()))
    x1.append(_x1)
    y1.append(_y1)
    x2.append(_x2)
    y2.append(_y2)

    # OFFSET을 더해줍니다.
    x1[i] += OFFSET
    y1[i] += OFFSET
    x2[i] += OFFSET
    y2[i] += OFFSET

# 직사각형에 주어진 순으로 1, 2 번호를 붙여줍니다.
# 격자 단위로 진행하는 문제이므로
# x2, y2에 등호가 들어가지 않음에 유의합니다.
for i in range(n):
    for x in range(x1[i], x2[i]):
        for y in range(y1[i], y2[i]):
            checked[x][y] = 1 if i % 2 == 0 else 2

# 숫자 2로 남아있는 영역의 넓이를 구합니다.
area = 0
for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if checked[x][y] == 2:
            area += 1

print(area)
