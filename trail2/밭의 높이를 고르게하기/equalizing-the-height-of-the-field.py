n,  h,t = map(int, input().split())
arr = list(map(int, input().split()))

ans = float('inf')

for i in range(n - t + 1):
    cost = 0

    for j in range(i, i + t):
        cost += abs(arr[j] - h)

    ans = min(ans, cost)

print(ans)