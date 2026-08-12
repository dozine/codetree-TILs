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

# n = int(input())
# arr = list(map(int, input().split()))

# cnt = 0

# for i in range(n):
#     for j in range(i, n):
#         total = sum(arr[i:j+1])
#         length = j - i + 1
#         if (total/length) in arr[i:j+1]:
#             cnt += 1

# print(cnt)

n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    sum_interval = 0
    nums = set()
    for j in range(i, n):
        sum_interval += arr[j]
        nums.add(arr[j])
        length = j - i + 1

        if sum_interval % length == 0:
            avg = sum_interval // length
            if avg in nums:
                cnt += 1

print(cnt)