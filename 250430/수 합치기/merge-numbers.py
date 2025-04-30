import heapq

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)  # 리스트를 최소 힙으로 변환 (O(N))

ans = 0

while len(arr) > 1:
    a = heapq.heappop(arr)  # 가장 작은 수
    b = heapq.heappop(arr)  # 그 다음 작은 수
    cost = a + b
    ans += cost
    heapq.heappush(arr, cost)  # 합친 값을 다시 힙에 넣음

print(ans)
