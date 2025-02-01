# 변수 선언 및 입력
n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# 주어진 시작점에서 연속된 같은 숫자가 끝나는 위치를 찾는 함수
def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx - 1
    return len(numbers) - 1

while True:
    did_explode = False
    exploded_numbers = [False] * len(numbers)  # 터진 폭탄을 표시할 리스트

    for curr_idx, number in enumerate(numbers):
        if exploded_numbers[curr_idx]:  # 이미 터진 폭탄이면 스킵
            continue

        end_idx = get_end_idx_of_explosion(curr_idx, number)

        if end_idx - curr_idx + 1 >= m:  # 연속된 개수가 m 이상이면 폭발
            for i in range(curr_idx, end_idx + 1):
                exploded_numbers[i] = True  # 터진 곳을 표시
            did_explode = True

    # 새로운 리스트를 만들어서 터지지 않은 폭탄만 남김
    new_numbers = []
    for i in range(len(numbers)):
        if not exploded_numbers[i]:  # 터지지 않은 숫자만 추가
            new_numbers.append(numbers[i])

    numbers = new_numbers  # 리스트 갱신

    if not did_explode:  # 폭발이 더 이상 일어나지 않으면 종료
        break

# 결과 출력
print(len(numbers))
for number in numbers:
    print(number)
