n = int(input())
arr = list(map(int, input().split()))

arr.sort()  # 오름차순 정렬

group_max = 0
for i in range(n):
    group_sum = arr[i] + arr[-(i + 1)]  # 앞쪽과 뒤쪽의 요소를 묶음
    group_max = max(group_max, group_sum)  # 그룹의 합 중 최댓값 갱신

print(group_max)