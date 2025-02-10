N = int(input())

selected_nums = []
visited = [False] * (N + 1)  # 방문 체크 배열

def print_permutation():
    for num in selected_nums:
        print(num, end=" ")
    print()

def find_permutation(cnt):
    if cnt == N:
        print_permutation()
        return
    for i in range(N, 0, -1):  # 큰 숫자부터 탐색!
        if not visited[i]:  
            visited[i] = True
            selected_nums.append(i)
            find_permutation(cnt + 1)
            selected_nums.pop()
            visited[i] = False

find_permutation(0)
