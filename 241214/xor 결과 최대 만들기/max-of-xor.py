n, m = map(int, input().split())
nums = list(map(int, input().split()))

max_xor = 0  # XOR 결과의 최대값을 저장하는 변수

def backtrack(start, count, current_xor):
    global max_xor
    
    # 숫자 m개를 모두 선택한 경우
    if count == m:
        max_xor = max(max_xor, current_xor)  # 최대값 갱신
        return

    # 가능한 숫자를 선택 (start부터 n까지)
    for i in range(start, n):
        # 현재 숫자를 선택하고 XOR 계산
        backtrack(i + 1, count + 1, current_xor ^ nums[i])

# 백트래킹 시작
backtrack(0, 0, 0)

# 결과 출력
print(max_xor)
