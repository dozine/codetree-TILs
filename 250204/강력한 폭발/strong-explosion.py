n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 폭탄이 놓일 수 있는 위치를 저장
bomb_pos = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

# 폭탄 타입별 영향 범위
bomb_patterns = [
    [],
    [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],  # 1번 폭탄 (세로 직선)
    [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],  # 2번 폭탄 (십자 모양)
    [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]] # 3번 폭탄 (대각선)
]

# 폭탄이 터진 위치를 저장할 배열 (초기화: 0)
is_bombed = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def apply_bomb(x, y, bomb_type, delta):
    """
    폭탄을 배치하거나 원상 복구 (delta=+1: 배치, -1: 원상 복구)
    """
    for dx, dy in bomb_patterns[bomb_type]:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            is_bombed[nx][ny] += delta  # 영향 반영 (중복 처리)

def count_bombed():
    """초토화된 영역 수 계산"""
    return sum(1 for i in range(n) for j in range(n) if is_bombed[i][j] > 0)

def backtracking(cnt, max_val):
    """백트래킹으로 최대 초토화 영역 찾기"""
    if cnt == len(bomb_pos):  # 모든 폭탄을 배치했을 때
        return max(max_val, count_bombed())

    x, y = bomb_pos[cnt]  # 현재 폭탄 배치 위치

    for bomb_type in range(1, 4):  # 폭탄 타입 (1~3번)
        apply_bomb(x, y, bomb_type, 1)  # 폭탄 배치
        max_val = backtracking(cnt + 1, max_val)
        apply_bomb(x, y, bomb_type, -1)  # 원상 복구

    return max_val

# 백트래킹 실행
result = backtracking(0, 0)
print(result)
