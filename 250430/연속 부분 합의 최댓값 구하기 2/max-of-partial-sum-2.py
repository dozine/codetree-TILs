# n = int(input())
# a = list(map(int, input().split()))

# current_sum = 0
# max_sum = a[0]  # 첫 원소로 초기화

# for num in a:
#     current_sum = max(num, current_sum + num)
#     max_sum = max(max_sum, current_sum)

# print(max_sum)

import sys

INT_MIN = -sys.maxsize


n = int(input())
arr = [0] + list(map(int, input().split()))

ans = INT_MIN

sum_of_nums = 0;

for i in range(1, n + 1):
    if sum_of_nums < 0:
        sum_of_nums = arr[i]
    else:
        sum_of_nums += arr[i]
    
    ans = max(ans, sum_of_nums)

print(ans)
