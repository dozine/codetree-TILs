n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
coins.sort(reverse=True)
ans=0
for coin in coins:
    ans+=k//coin
    k%=coin

print(ans)