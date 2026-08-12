# n=int(input())
# arr=list(map(int,input().split()))

# cnt=0
# for i in range(n):
#     for j in range(i,n):
#         sum_interval=0
#         for k in range(i,j+1):
#             sum_interval+=arr[k]
#         avg =sum_interval/(j-i+1)
#         exists=False
#         for k in range(i,j+1):
#             if arr[k]==avg:
#                 exists=True
        
#         if exists:
#             cnt+=1
# print(cnt)

n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i, n):
        total = sum(arr[i:j+1])
        length = j - i + 1

        if total % length == 0:
            avg = total // length

            if avg in arr[i:j+1]:
                cnt += 1

print(cnt)