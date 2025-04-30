n = int(input())
a = list(map(int, input().split()))

current_sum = 0
max_sum = a[0]  # 첫 원소로 초기화

for num in a:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print(max_sum)
