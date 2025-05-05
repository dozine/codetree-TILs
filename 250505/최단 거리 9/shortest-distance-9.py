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

path = [0] * (n + 1)

# 그래프를 인접행렬로 표현
# 양방향 그래프이므로 양쪽 다 표시해줍니다.
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x][y] = z
    graph[y][x] = z

# 시작, 끝 위치를 입력으로 받습니다.
a, b = tuple(map(int, input().split()))

# 시작위치에는 dist값을 0으로 설정
dist[a] = 0

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

        if dist[j] > dist[min_index] + graph[min_index][j]:
            dist[j] = dist[min_index] + graph[min_index][j]
            # path값을 갱신해줍니다.
            path[j] = min_index

# 정점 A에서 정점 B로 가기 위한 최단거리를 출력합니다.
print(dist[b])

# 도착지 B에서 시작하여
# 시작점 A가 나오기 전까지
# path를 따라 움직여줍니다.
x = b
vertices = []
vertices.append(x)

while x != a:
    x = path[x]
    vertices.append(x)

# 거쳐간 순서를 거꾸로 출력합니다.
for num in vertices[::-1]:
    print(num, end=" ")



# import sys
# import heapq

# INT_MAX = sys.maxsize

# # 입력 받기
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# dist = [INT_MAX] * (n + 1)
# path = [0] * (n + 1)

# # 간선 정보 입력 (인접리스트 방식)
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z))
#     graph[y].append((x, z))  # 양방향 그래프

# # 시작, 도착 정점
# a, b = map(int, input().split())

# # 우선순위 큐 시작 설정
# dist[a] = 0
# pq = [(0, a)]  # (거리, 노드번호)

# while pq:
#     cur_dist, cur = heapq.heappop(pq)

#     # 이미 더 짧은 거리로 방문한 적 있다면 스킵
#     if cur_dist > dist[cur]:
#         continue

#     for neighbor, weight in graph[cur]:
#         new_dist = dist[cur] + weight
#         if new_dist < dist[neighbor]:
#             dist[neighbor] = new_dist
#             path[neighbor] = cur
#             heapq.heappush(pq, (new_dist, neighbor))

# # 최단 거리 출력
# print(dist[b])

# # 경로 복원
# x = b
# vertices = []
# while x:
#     vertices.append(x)
#     x = path[x]

# # 경로 출력 (역순)
# print(*reversed(vertices))


## 아래 코드는 우선순위 큐를 적용한 코드임 

