n, m, k = map(int, input().split())
arr = [
    int(input())
    for _ in range(m)
]

punish = [0] * (n+1)

ans = 0
for i in arr:
    punish[i] += 1 
    if punish[i] >= k:
        ans = i
        break
print(ans)