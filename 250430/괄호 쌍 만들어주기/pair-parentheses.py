# A = input()

# cnt = 0
# n = len(A)

# for i in range(n-1):  # n-1까지만 가야 A[i+1] 접근 가능
#     if A[i] == '(' and A[i+1] == '(':  # (( 찾기
#         for j in range(i+2, n-1):  # i+2부터 n-2까지 검사
#             if A[j] == ')' and A[j+1] == ')':  # )) 찾기
#                 cnt += 1

# print(cnt)


# A = input()

# cnt = 0

# for i in range(len(A) - 1):
#     if A[i] == "(" and A[i+1] == "(":
#         for j in range(i + 2, len(A) - 1):
#             if A[j] == ")" and A[j+1] == ")":
#                 cnt += 1

# print(cnt)

# 변수 선언 및 입력:
string = input()
n = len(string)
R = [0] * n

# R 배열을 채워줍니다.
# Ri = i번지부터 N - 1번지 까지 있는 문자열중에 
#      연속하여 ))가 나오는 횟수
R[n - 1] = 0
for i in range(n - 2, -1, -1):
    # i, i + 1로 )) 조합이 만들어진다면
    # i번부터 만들 수 있는 조합 수가 1만큼 더 늘어납니다.
    if string[i] == ')' and string[i + 1] == ')':
        R[i] = R[i + 1] + 1
    # 그렇지 않다면, i + 1번부터 만들 수 있는 조합 수와 같습니다.
    else:
        R[i] = R[i + 1]

# 답을 구해줍니다.
# 현재 i, i + 1 조합과
# 쌍을 이루는 서로 다른 가짓수를 세어
# 답에 더해줍니다.
ans = 0
for i in range(n - 2):
    if string[i] == '(' and string[i + 1] == '(':
        ans += R[i + 2]

print(ans)
