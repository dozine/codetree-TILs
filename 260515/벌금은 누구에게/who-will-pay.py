# n, m, k = map(int, input().split())
# arr = [
#     int(input())
#     for _ in range(m)
# ]

# punish = [0] * (n+1)

# ans = -1
# for i in arr:
#     punish[i] += 1 
#     if punish[i] >= k:
#         ans = i
#         break
# print(ans)

n,m,k = list(map(int,input().split()))
arr = [0] * (n+1)

ans = -1
for i in range(1,m+1):
    student = int(input())
    arr[student]+=1
    if arr[student]==k:
        ans = student 
        break
        
print(ans)
    

