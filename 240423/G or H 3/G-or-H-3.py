MAX_NUM=10000
n,k=tuple(map(int,input().split()))
arr=[0] * (MAX_NUM+1)
for _ in range(n):
    x,c=tuple(input().split())
    x=int(x)
    arr[x] =1 if c=='G' else 2
max_sum=0
for i in range(MAX_NUM-k+1):
    sum_interval=0
    for j in range(i,i+k+1):
        sum_interval += arr[j]
    max_sum=max(max_sum,sum_interval)
print(max_sum)