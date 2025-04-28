n, k = map(int, input().split())
arr = list(map(int, input().split()))
ps=[0]*(n+1)
# Please write your code here.
for i in range(n-k+1):
    for j in range(i,i+k):
        ps[i]+=arr[j]

answer=max(ps)
print(answer) 