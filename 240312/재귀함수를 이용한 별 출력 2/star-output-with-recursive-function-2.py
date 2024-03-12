def recursive_fun_minus(n):
    n = int(n)
    print("* " * n)
    if n == 1:
        return 1
    return recursive_fun_minus(n - 1)

def recursive_fun_plus(n, end):
    n = int(n)
    print("* " * n)
    if n == end:
        return
    return recursive_fun_plus(n + 1, end)

n = int(input())
first_result = recursive_fun_minus(n)
recursive_fun_plus(first_result, n)