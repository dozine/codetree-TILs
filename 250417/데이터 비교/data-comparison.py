n = int(input())
arr1 = set(map(int, input().split()))  # set으로 중복 제거 및 빠른 검색

m = int(input())
arr2 = list(map(int, input().split()))  # 순서를 보존하기 위해 list 사용

for num in arr2:
    if num in arr1:
        print(1, end=" ")
    else:
        print(0, end=" ")