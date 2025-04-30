A = input()

cnt = 0
n = len(A)

for i in range(n-1):  # n-1까지만 가야 A[i+1] 접근 가능
    if A[i] == '(' and A[i+1] == '(':  # (( 찾기
        for j in range(i+2, n-1):  # i+2부터 n-2까지 검사
            if A[j] == ')' and A[j+1] == ')':  # )) 찾기
                cnt += 1

print(cnt)
