# n,m=tuple(map(int,input().split()))
# x,y=[
#     tuple(map(int,input().split()))
#     for _ in range(m)
# ]

# def dfs(v):
#     for curr_v in range(1,n+1):
#         if graph[vertex][curr_v] and no vi
from collections import deque

def count_reachable_nodes(n, m, edges):
    # 그래프 초기화
    graph = {i: [] for i in range(1, n+1)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    # BFS 탐색
    visited = set()
    queue = deque([1])  # 1번 정점에서 시작
    visited.add(1)
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # 1번 정점을 제외한 도달 가능한 정점의 개수
    return len(visited) - 1

# 입력 받기
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(count_reachable_nodes(n, m, edges))
