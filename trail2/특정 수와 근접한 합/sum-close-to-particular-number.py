n, s = map(int, input().split())
arr = list(map(int, input().split()))

total = sum(arr)

ans = float('inf')

for i in range(n):
    for j in range(i + 1, n):

        current = total - arr[i] - arr[j]
        diff = abs(s - current)

        ans = min(ans, diff)

print(ans)