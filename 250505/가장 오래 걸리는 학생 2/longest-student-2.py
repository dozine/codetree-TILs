import sys 
INT_MAX=sys.maxsize

import heapq

n,m=tuple(map(int,input().split()))
graph=[
    []for _ in range(n+1)
]
dist=[INT_MAX]*(n+1)
pq=[]

for _ in range(m):
    x,y,z=tuple(map(int,input().split()))
    graph[x].append((y,z))
    graph[y].append((x,z))

dist[n]=0
heapq.heappush(pq,(0,n))

while pq:
    min_dist,min_index=heapq.heappop(pq)
    
    if min_dist!=dist[min_index]:
        continue
    for target_index,target_dist in graph[min_index]:
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))

max_time = 0
for i in range(1, n):
    if dist[i] == INT_MAX:
        continue 
    max_time = max(max_time, dist[i])

print(max_time)