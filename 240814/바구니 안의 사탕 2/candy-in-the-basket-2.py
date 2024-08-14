max_num=100
n,k=tuple(map(int,input().split()))
arr=[0]*(max_num+1)

for _ in range(n):
    a,x=tuple(map(int,input().split()))
    arr[x]+=a

max_sum=0
for i in range(max_num):
    sum_all=0
    for j in range(i-k,i+k+1):
        if j>=0 and j<=max_num:
            sum_all += arr[j]
    
    max_sum=max(max_sum,sum_all)

print(max_sum)