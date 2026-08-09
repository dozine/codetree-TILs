# import sys
# INT_MIN=-sys.maxsize
# n=int(input())
# arr=list(map(int,input().split()))
# ans=INT_MIN
# for i in range(n):
#     for j in range(i+2,n):
#         if ans < arr[i] +arr[j]:
#             ans =arr[i] +arr[j]
# print(ans)

n =int(input())
arr = list(map(int,input().split()))

max_ans = -1
for i in range(n):
    for j in range(i+2,n):
            sum = arr[i]+arr[j]
            max_ans = max(sum, max_ans) 

print(max_ans)