import sys
INT_MAX=sys.maxsize

arr=list(map(int,input().split()))

def diff(i,j,k):
    sum1=arr[i]+arr[j]+arr[k]
    sum2=sum(arr)-sum1
    return abs(sum1-sum2)

min_diff=INT_MAX
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            min_diff=min(min_diff,diff(i,j,k))

print(min_diff)