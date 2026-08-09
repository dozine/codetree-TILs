from collections import deque

n = int(input())
arr = [int(input()) for _ in range(n)]


def is_carry(x, y, z):
    str_x = deque(str(x))
    str_y = deque(str(y))
    str_z = deque(str(z))

    while max(len(str_x), len(str_y), len(str_z)):

        if len(str_x) > 0:
            x = int(str_x.pop())
        else:
            x = 0

        if len(str_y) > 0:
            y = int(str_y.pop())
        else:
            y = 0

        if len(str_z) > 0:
            z = int(str_z.pop())
        else:
            z = 0

        if x + y + z >= 10:
            return False

    return True


max_ans = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if is_carry(arr[i], arr[j], arr[k]):
                ans = arr[i] + arr[j] + arr[k]
                max_ans = max(ans, max_ans)

print(max_ans)