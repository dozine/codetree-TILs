n = int(input())  # 블록 개수
blocks = [int(input()) for _ in range(n)]  # 블록 리스트
s1, e1 = map(int, input().split())  # 첫 번째 플레이어의 범위
s2, e2 = map(int, input().split())  # 두 번째 플레이어의 범위

# 첫 번째 플레이어의 범위를 제거
remaining_blocks = blocks[1:s1] + blocks[e1:]

# 두 번째 플레이어의 범위를 제거
remaining_blocks = remaining_blocks[1:s2] + remaining_blocks[e2:]

# 결과 출력
print(len(remaining_blocks))
for i in remaining_blocks:
    print(i)

