n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
coins.sort(reverse=True)
ans=0
for coin in coins:
    ans+=k//coin
    k%=coin

print(ans)

coins.sort(reverse=True)
#coin을 일단 내림차 순으로 정렬 하고 

for coin in coins:
    ans+=k//coin # K원을 구성하는 coin원의 개수가 최소가 되는 거랑께
    k%=coin #k%coin하면 나머지 금액이 나오니깐 그걸 k에 넣으삼. ㅎㅎ 