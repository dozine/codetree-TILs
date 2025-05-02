MAX_NUM = 100000

n, m = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]


def is_possible(k):
    cnt = 0
    for elem in arr:
        cnt += elem // k
    return cnt >= m


left = 1                          # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
right = MAX_NUM                   # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = 0                           # 답을 저장합니다.

while left <= right:              # [left, right]가 유효한 구간이면 계속 수행합니다.
    mid = (left + right) // 2     # 가운데 위치를 선택합니다.
    if is_possible(mid):          # 결정문제에 대한 답이 Yes라면
        left = mid + 1            # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 left를 바꿔줍니다.
        ans = max(ans, mid)       # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:                               
        right = mid - 1           # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

print(ans)
