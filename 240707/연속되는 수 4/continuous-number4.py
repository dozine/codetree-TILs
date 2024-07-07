n=int(input())
arr=[
    int(input())
    for _ in range(n)
]

cnt,ans=0,0
for i in range(n):
    if arr[i-1]<arr[i]:
        cnt+=1
    else: 
        cnt=1
    ans=max(ans,cnt)
print(ans)