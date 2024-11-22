# def remove_bombs(bombs, m):
#     while True:
#         n = len(bombs)
#         to_remove = set()
#         start = 0
        
#         while start < n:
#             end = start
#             while end < n and bombs[end] == bombs[start]:
#                 end += 1
#             if end - start >= m:
#                 to_remove.update(range(start, end))
#             start = end
#         if not to_remove:
#             break  
#         bombs = [bombs[i] for i in range(n) if i not in to_remove]
    
#     return bombs
# n, m = map(int, input().split())
# bombs = [int(input()) for _ in range(n)]
# result = remove_bombs(bombs, m)

# print(len(result))
# for bomb in result:
#     print(bomb)

def process_bombs(n, m, bombs):
    stack = []  # 스택 초기화
    for bomb in bombs:
        # 스택의 마지막 요소와 현재 폭탄이 같으면 스택에 추가
        if stack and stack[-1][0] == bomb:
            stack[-1][1] += 1
        else:
            stack.append([bomb, 1])  # 새로운 폭탄 숫자를 스택에 추가
        
        # 연속된 폭탄 개수가 M 이상이면 제거
        if stack[-1][1] >= m:
            stack.pop()
    
    # 결과를 스택에서 다시 추출
    result = []
    for num, count in stack:
        result.extend([num] * count)
    return result

# 입력 처리
n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]

# 폭탄 처리
result = process_bombs(n, m, bombs)

# 출력
print(len(result))
for bomb in result:
    print(bomb)
