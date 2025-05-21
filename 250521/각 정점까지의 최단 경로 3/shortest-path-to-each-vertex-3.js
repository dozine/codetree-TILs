import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

# 그래프에 있는 모든 노드들에 대해
# 초기값을 전부 아주 큰 값으로 설정
dist = [INT_MAX] * (n + 1) 

# 그래프를 인접행렬로 표현
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x][y] = z

# 시작위치에는 dist값을 0으로 설정
dist[1] = 0

# O(|V|^2) 다익스트라 코드
for i in range(1, n + 1):
    # V개의 정점 중 
    # 아직 방문하지 않은 정점 중
    # dist값이 가장 작은 정점을 찾아줍니다.
    min_index = -1
    for j in range(1, n + 1):
        if visited[j]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    # 최솟값에 해당하는 정점에 방문 표시를 진행합니다.
    visited[min_index] = True

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최단거리 값을 갱신해줍니다.
    for j in range(1, n + 1):
        # 간선이 존재하지 않는 경우에는 넘어갑니다.
        if graph[min_index][j] == 0:
            continue

        dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])

# 시작점(1번 정점)으로부터 각 지점까지의 최단거리 값을 출력합니다.
for i in range(2, n + 1):
    # 만약 도달이 불가능하다면 -1을 출력합니다.
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])
