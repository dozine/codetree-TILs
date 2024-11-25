# 입력 처리
n, curr_x, curr_y = map(int, input().split())  # 격자의 크기와 시작 위치
a = [[0] * (n + 1)]  # 격자의 1번 인덱스부터 시작하도록 설정
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

# 방문한 숫자를 저장할 리스트
visited_nums = []

# 격자 범위 확인 함수
def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

# 이동 가능 여부 확인 함수
def can_go(x, y, curr_num):
    return in_range(x, y) and a[x][y] > curr_num

# 이동 함수
def simulate():
    global curr_x, curr_y
    # 상하좌우 이동 방향
    dx = [-1, 1, 0, 0]  # 위, 아래
    dy = [0, 0, -1, 1]  # 왼쪽, 오른쪽
    
    # 4방향을 탐색하며 이동 가능한 곳 찾기
    for i in range(4):
        next_x, next_y = curr_x + dx[i], curr_y + dy[i]
        if can_go(next_x, next_y, a[curr_x][curr_y]):
            curr_x, curr_y = next_x, next_y  # 위치 이동
            return True  # 이동 성공
    return False  # 이동 실패

# 초기 위치의 숫자 추가
visited_nums.append(a[curr_x][curr_y])

# 이동 시뮬레이션 반복
while simulate():
    visited_nums.append(a[curr_x][curr_y])  # 이동한 위치의 숫자 추가

# 결과 출력
print(" ".join(map(str, visited_nums)))
