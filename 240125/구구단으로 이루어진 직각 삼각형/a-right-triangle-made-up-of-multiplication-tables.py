N= int(input())
for i in range(1, N + 1):
    for j in range(1, N - i + 2):
        print(f"{i} * {j} = {i * j}", end="")
        
        if j != (N - i + 1):
            print(" / ", end="")
    print()