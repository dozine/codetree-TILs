n = int(input())
a = list(map(int, input().split()))

ans = -float('inf')  # 음수만 있을 수 있으므로 초기값을 아주 작은 수로 설정
for i in range(n):
    total = 0
    for j in range(i, n):
        total += a[j]
        ans = max(ans, total)

print(ans)
