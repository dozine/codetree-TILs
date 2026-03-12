# 1. 입력 받기
a, b = map(int, input().split())
n_str = input()

# 2. A진수(문자열/리스트) -> 10진수 변환 함수
def to_decimal(n_str, a):
    num = 0
    for char in n_str:
        num = num * a + int(char)
    return num

# 3. 10진수 -> B진수 변환 함수
def from_decimal(n, b):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % b)
        n //= b
    return digits[::-1] # 역순으로 뒤집기

# 4. 변환 실행
decimal_value = to_decimal(n_str, a)
result_b_base = from_decimal(decimal_value, b)

# 5. 출력
print(*result_b_base, sep='')