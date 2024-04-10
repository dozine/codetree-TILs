n,m,k=tuple(map(int,input().split()))
num=[
    int(input())
    for _ in range(m)
]
penalty=[0]*(n+1)

ans = -1
for i in num:
    penalty[i] +=1
    if penalty[i] >=k:
        ans=i
        break
print(ans)