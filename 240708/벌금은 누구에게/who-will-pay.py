n,m,k=tuple(map(int,input().split()))
person=[
    int(input())
    for _ in range(m)
]

penalty=[0]*(n+1)

ans=-1
for t in person:
    penalty[t] +=1
    if penalty[t] >= k:
        ans=t
        break
print(ans)