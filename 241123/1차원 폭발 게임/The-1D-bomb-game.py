def remove_bombs(bombs, m):
    while True:
        n = len(bombs)
        to_remove = set()
        start = 0
        
        while start < n:
            end = start
            while end < n and bombs[end] == bombs[start]:
                end += 1
            if end - start >= m:
                to_remove.update(range(start, end))
            start = end
        if not to_remove:
            break  
        bombs = [bombs[i] for i in range(n) if i not in to_remove]
    
    return bombs
n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]
result = remove_bombs(bombs, m)

print(len(result))
for bomb in result:
    print(bomb)
