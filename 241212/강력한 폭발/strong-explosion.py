# 입력 및 초기화
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bomb_types = [  # 폭탄 종류별 폭발 패턴
    [],
    [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],  # 세로 폭발
    [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],  # 십자형 폭발
    [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]  # 대각선 폭발
]

affected = [[False] * n for _ in range(n)]  # 폭발로 영향을 받은 칸
bomb_positions = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]  # 폭탄 배치 가능한 칸
current_types = [[0] * n for _ in range(n)]  # 현재 폭탄 배치 상태
max_area = 0  # 최대 초토화 영역


# 좌표 유효성 확인
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n


# 폭탄 설치 및 폭발 처리
def explode(x, y, bomb_type):
    for dx, dy in bomb_types[bomb_type]:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            affected[nx][ny] = True


# 초토화 영역 계산
def calculate_area():
    # 폭발 영향을 초기화
    for i in range(n):
        for j in range(n):
            affected[i][j] = False

    # 각 폭탄 배치에 따라 폭발 처리
    for i in range(n):
        for j in range(n):
            if current_types[i][j] > 0:  # 폭탄이 배치된 경우
                explode(i, j, current_types[i][j])

    # 영향을 받은 칸 개수 계산
    return sum(sum(row) for row in affected)


# 폭탄 배치를 위한 재귀 탐색
def find_max_bomb_area(pos_index):
    global max_area

    if pos_index == len(bomb_positions):  # 모든 폭탄 배치를 완료한 경우
        max_area = max(max_area, calculate_area())
        return

    x, y = bomb_positions[pos_index]

    for bomb_type in range(1, 4):  # 폭탄 종류 1~3
        current_types[x][y] = bomb_type
        find_max_bomb_area(pos_index + 1)
        current_types[x][y] = 0  # 원상 복구


# 폭탄 배치 및 결과 출력
find_max_bomb_area(0)
print(max_area)
