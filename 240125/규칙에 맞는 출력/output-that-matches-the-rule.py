n=int(input())
for i in range(n, 0, -1):
    for k in range(i, n + 1):
        print(k, end=" ")
    print()