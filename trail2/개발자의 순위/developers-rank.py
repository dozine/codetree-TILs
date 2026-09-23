# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(k)
]

ans = 0

# 모든 쌍에 대해서 불변의 순위인 쌍을 찾습니다.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # i번 개발자가 j번 개발자보다 항상 높은 순위인지 여부를 확인합니다.

        # i와 j가 같을 경우 넘어갑니다.
        if i == j:
            continue
            
        # correct : i번 개발자가 j번 개발자보다 항상 높은 순위일때 true
        correct = True

        # k번의 모든 경기에 대해서 두 개발자의 위치를 찾고,
        # 하나라도 i번 개발자가 더 뒤에 있으면 correct를 false로 바꿉니다.
        for lists in arr:
            index_i = lists.index(i)
            index_j = lists.index(j)

            if index_i > index_j:
                correct = False

        if correct:
            ans += 1
    
print(ans)


