N, B = map(int, input().split())

def solution(n, b):
    if n == 0:
        return [0]
    
    digits = []
    while n > 0:
        # 1. n을 b로 나눈 나머지를 자릿수로 추가
        digits.append(n % b)
        # 2. n을 b로 나눈 몫으로 갱신
        n = n // b
        
    # 나머지가 역순으로 담기므로 뒤집어줍니다.
    return digits[::-1]

# 리스트 요소를 공백 없이 출력
result = solution(N, B)
print(*(result), sep='')