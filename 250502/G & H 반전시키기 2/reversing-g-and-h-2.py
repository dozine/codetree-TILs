# 변수 선언 및 입력:

n = int(input())
a = input()
b = input()

# 뒤에서부터 선택을 진행합니다.
# 현재 위치에서 꼭 눌러야만
# 문제 조건을 만족시킬 수 있다면
# 눌러주고 넘어갑니다.
cnt = 0
for i in range(n - 1, -1, -1):
    # 두 문자가 다른 경우이면서
    # 지금까지 뒤에서 눌렀던 횟수가 짝수번이라
    # i번째 문자에 영향을 주지 못하는 경우라면
    # 현재 위치를 선택해줘야 합니다.
    if a[i] != b[i] and cnt % 2 == 0:
        cnt += 1
    
    # 두 문자가 같은 경우이면서
    # 지금까지 뒤에서 놀렀던 횟수가 홀수번이라
    # i번째 문자에 영향을 주는 경우라면
    # 현재 위치를 선택해줘야 합니다.
    elif a[i] == b[i] and cnt % 2 == 1:
        cnt += 1

print(cnt)
