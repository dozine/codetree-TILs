import sys 
INT_MAX=sys.maxsize
n=int(input())
arr=list(map(int,input().split()))

min_diff=INT_MAX
for i in range(n):
    arr[i]*=2
    for j in range(n):
        new_arr=[]
        for k in range(n):
            if k!=j:
                new_arr.append(arr[k])
        sum_diff=0
        for k in range(n-2):
            sum_diff+=abs(new_arr[k+1]-new_arr[k])
        min_diff=min(min_diff,sum_diff)
    arr[i]//=2
print(min_diff)