n=int(input())
time=[
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans=0
for i in range(n):
    working=[0]*1000
    for j,(x,y) in enumerate(time):
        if j==i:
            continue
        for k in range(x,y):
            working[k]+=1
    t=0
    for j in range(1,1000):
        if working[j]>0:
            t+=1
    ans=max(ans,t)
print(ans)