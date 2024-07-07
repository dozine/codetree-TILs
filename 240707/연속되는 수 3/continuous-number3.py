n=int(input())

arr=[
    int(input())
    for _ in range(n)
]

ans,cnt=0,0
for i in range(n):
    if (arr[i]>0 and arr[i-1]>0) or (arr[i]<0 and arr[i-1]<0):
        cnt+=1
    else: 
        cnt=1
    ans=max(cnt,ans)
print(ans)