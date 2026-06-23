n, m = map(int, input().split())

# 1. 수정 가능한 2차원 리스트 형태로 격자를 공백(" ")으로 초기화합니다.
arr = [
    [" "] * m
    for _ in range(n)
]

# 문제 조건: 오른쪽(0) -> 아래쪽(1) -> 왼쪽(2) -> 위쪽(3)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

cur_dir = 0 
x, y = 0, 0

# 격자 범위 체크 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 총 N * M개의 칸을 채웁니다. (0번째 칸부터 시작하므로 글자 수만큼 루프)
for i in range(n * m):
    # 2. 현재 위치 (x, y)에 알파벳을 채웁니다.
    # 아스키코드 65('A')에 i를 26으로 나눈 나머지를 더해 Z 이후 A로 순환하게 만듭니다.
    arr[x][y] = chr(65 + (i % 26))
    
    # 마지막 칸을 채웠다면 다음 칸을 계산할 필요 없이 종료합니다.
    if i == n * m - 1:
        break
        
    # 현재 방향으로 다음 위치를 미리 계산해봅니다.
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    
    # 격자를 벗어나거나, 이미 알파벳이 채워진 칸(" "이 아닌 칸)을 만나면 방향 회전
    if not in_range(nx, ny) or arr[nx][ny] != " ":
        cur_dir = (cur_dir + 1) % 4
        
    # 확정된 방향으로 좌표를 이동시킵니다.
    x, y = x + dxs[cur_dir], y + dys[cur_dir]

# 3. 출력: 행(n)과 열(m) 크기에 맞게 출력합니다.
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()