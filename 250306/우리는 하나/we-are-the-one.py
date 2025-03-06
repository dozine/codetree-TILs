from itertools import combinations
import sys
from collections import deque

input = sys.stdin.readline

# 1. 입력 받기
N, K, U, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 2. 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 3. BFS 함수: 특정 시작점에서 이동 가능한 도시 개수 구하기
def bfs(start_x, start_y, visited_global):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    visited_global.add((start_x, start_y))
    count = 1  # 시작점 포함

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                height_diff = abs(grid[x][y] - grid[nx][ny])
                if U <= height_diff <= D:  # 이동 가능 조건
                    visited[nx][ny] = True
                    visited_global.add((nx, ny))
                    queue.append((nx, ny))
                    count += 1

    return count

# 4. 모든 도시 좌표 리스트 생성
city_positions = [(i, j) for i in range(N) for j in range(N)]

# 5. K개의 도시를 선택하는 조합을 생성하여 최대 방문 가능한 도시 수 탐색
max_city_count = 0
for selected_cities in combinations(city_positions, K):
    visited_global = set()
    total_count = 0
    
    for x, y in selected_cities:
        if (x, y) not in visited_global:
            count = bfs(x, y, visited_global)
            total_count += count
    
    max_city_count = max(max_city_count, total_count)

# 6. 결과 출력
print(max_city_count)
