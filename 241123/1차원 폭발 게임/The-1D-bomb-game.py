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
    while True:
        new_bombs = []
        count = 1
        exploded = False

        # 현재 폭탄 리스트를 순회하며 연속 숫자 그룹 확인
        for i in range(1, len(bombs)):
            if bombs[i] == bombs[i - 1]:  # 연속 숫자
                count += 1
            else:  # 연속이 끊기면 처리
                if count >= m:  # 연속된 숫자가 M개 이상이면 제거
                    exploded = True
                else:  # 제거되지 않은 숫자는 유지
                    new_bombs.extend(bombs[i - count:i])
                count = 1  # 새 그룹 시작

        # 마지막 그룹 처리
        if count >= m:
            exploded = True
        else:
            new_bombs.extend(bombs[len(bombs) - count:])

        # 폭발이 없었다면 종료
        if not exploded:
            break

        # 갱신된 폭탄 리스트로 업데이트
        bombs = new_bombs

    return bombs

# 입력 처리
n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]

# 폭탄 처리
result = process_bombs(n, m, bombs)

# 출력
print(len(result))
for bomb in result:
    print(bomb)
