import sys
INT_MAX=sys.maxsize
arr=list(map(int,input().split()))
n=6

def diff(i,j,k):
    sum1 = arr[i] + arr[j] +arr[k]
    sum2 = sum(arr) - sum1
    return abs(sum1 - sum2)

min_diff=INT_MAX
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            min_diff=min(min_diff,diff(i,j,k))
print(min_diff)