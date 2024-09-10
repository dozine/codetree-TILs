n,m,k=tuple(map(int,input().split()))
pernish=[
    int(input())
    for _ in range(m)
]
student=[0]*(n+1)


for i in pernish:
    student[i]+=1
    if student[i]>=k:
        ans=i
        break
    
print(i)