import sys

N = int(input())  # 도시 수
W = [list(map(int, input().split())) for _ in range(N)]  # 비용 행렬

min_cost = sys.maxsize
visited = [False] * N

def tsp(curr, start, count, cost):
    global min_cost

    # 모든 도시 방문 후 다시 시작점으로 돌아갈 때
    if count == N and W[curr][start] > 0:
        min_cost = min(min_cost, cost + W[curr][start])
        return

    for next in range(N):
        if not visited[next] and W[curr][next] > 0:
            visited[next] = True
            tsp(next, start, count + 1, cost + W[curr][next])
            visited[next] = False  # 백트래킹

# 모든 도시를 시작점으로 한 번씩 탐색
for start in range(N):
    visited[start] = True
    tsp(start, start, 1, 0)
    visited[start] = False

print(min_cost)
