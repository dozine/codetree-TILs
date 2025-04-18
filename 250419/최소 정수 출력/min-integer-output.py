import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
pq = []

for elem in x:
    if elem != 0:
        heapq.heappush(pq,elem)
    else:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq))
