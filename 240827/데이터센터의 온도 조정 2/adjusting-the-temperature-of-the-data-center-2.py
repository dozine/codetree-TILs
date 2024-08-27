n, c, g, h = map(int, input().split())
machine = [tuple(map(int, input().split())) for _ in range(n)]

def work(a):
    global n, c, g, h
    sum_val = 0
    for i in range(n):
        down, up = machine[i]
        if a < down:
            sum_val += c
        elif a > up:
            sum_val += h
        else:
            sum_val += g
    return sum_val

ans = 0
for i in range(1001):
    ans = max(ans, work(i))
print(ans)