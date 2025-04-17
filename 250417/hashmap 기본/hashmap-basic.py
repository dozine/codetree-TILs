
n = int(input())
d = dict()

for _ in range(n):
    command = input()

    if command.startswith("add"):
        _, k, v = tuple(command.split())
        k, v = int(k), int(v)
        d[k] = v
    elif command.startswith("remove"):
        k = int(command.split()[1])
        d.pop(k)
    else:
        k = int(command.split()[1])
        if k not in d:
            print("None")
        else:
            print(d[k])
