n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.

ans=0
for coin in coins[::-1]:
    ans+=k//coin
    k%=coin

print(ans)