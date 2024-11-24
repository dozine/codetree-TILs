# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_happy_sequence(sequence):
    consecutive_count, max_ccnt = 1, 1
    for i in range(1, len(sequence)):
        if sequence[i - 1] == sequence[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        max_ccnt = max(max_ccnt, consecutive_count)
    return max_ccnt >= m


num_happy = 0

# 먼저 가로로 행복한 수열의 수를 셉니다.
for row in grid:
    if is_happy_sequence(row):
        num_happy += 1

# 세로로 행복한 수열의 수를 셉니다.
for col in zip(*grid):
    if is_happy_sequence(col):
        num_happy += 1

print(num_happy)
        