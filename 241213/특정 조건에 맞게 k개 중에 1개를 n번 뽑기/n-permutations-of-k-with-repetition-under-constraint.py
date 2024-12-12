# k,n=tuple(map(int,input().split()))
# arr=[]

# def print_num():
#     for i in arr:
#         print(i,end=" ")
#     print()

# def find_num(cnt):
#     if cnt==n+1:
#         print_num()
#         return 

#     for i in range(1,n+1):
#         arr.append(i)
#         if arr[i]==arr[i+1] and arr[i+1]==arr[i+2]:
#             return False
#         find_num(cnt+1)
#         arr.pop()

# find_num(0)

from itertools import product

def is_valid_combination(comb):
    """
    주어진 조합이 조건을 만족하는지 확인합니다.
    조건: 연속하여 같은 숫자가 3번 이상 나오면 안 된다.
    """
    count = 1  # 연속된 숫자의 개수
    for i in range(1, len(comb)):
        if comb[i] == comb[i - 1]:
            count += 1
            if count >= 3:
                return False
        else:
            count = 1
    return True

def find_combinations(K, N):
    """
    1 이상 K 이하의 숫자를 N번 반복하여 나올 수 있는 모든 조합을 생성합니다.
    조건을 만족하는 조합만 반환합니다.
    """
    numbers = range(1, K + 1)  # 1부터 K까지의 숫자
    all_combinations = product(numbers, repeat=N)

    valid_combinations = [comb for comb in all_combinations if is_valid_combination(comb)]
    return valid_combinations

def main():
    # 입력 받기
    K, N = map(int, input().split())

    # 유효한 조합 찾기
    valid_combinations = find_combinations(K, N)

    # 출력하기
    for comb in valid_combinations:
        print(" ".join(map(str, comb)))

if __name__ == "__main__":
    main()
