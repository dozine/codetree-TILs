def modify_numbers(a, b):
    if a < b:
        a += 10
        b *= 2
    else:
        b += 10
        a *= 2
    return a, b


# 입력 예시
a, b = map(int, input().split())

# 함수 호출
a, b = modify_numbers(a, b)

# 출력 (함수 호출 이후)
print(a, b)
