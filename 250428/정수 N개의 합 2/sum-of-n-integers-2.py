n, k = map(int, input().split())
arr = list(map(int, input().split()))
ps=[0]*(n+1)
# Please write your code here.
for i in range(n-3):
    for k in range(i,i+3):
        ps[i]+=k

answer=max(ps)
print(answer) 