# n = int(input())
# A = list(map(int, input().split()))

# # Please write your code here.

n = int(input())
a = list(map(int,input().split()))


ans = float('inf')
for i in range(n): 
    total = 0
    for j in range(n):
        dis = abs(i-j) * a[j]
        total += dis 
    ans = min(ans,total)

print(ans)