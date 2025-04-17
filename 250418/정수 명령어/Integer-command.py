from sortedcontainers import SortedSet

t = int(input())
for _ in range(t):
    n = int(input())
    s = SortedSet()

    for _ in range(n):
        command, x = tuple(input().split())
        x = int(x)

        # treeset에 넣어줍니다.
        if command == 'I':
            s.add(x)
        # 큐가 비어있지 않을 경우에는 값을 제거해줍니다.
        elif command == 'D' and s:
            # x가 1이면 최댓값을 삭제합니다.
            if x == 1:
                s.remove(s[-1])
            # x가 -1이면 최솟값을 삭제합니다.
            else:
                s.remove(s[0])

    if not s:
        print("EMPTY")
    else:
        print(s[-1], s[0])
