# 배열에 주어진 수를 입력받아 저장합니다.
arr = list(map(int, input().split()))
sum2 = 0
sum3 = 0
cnt = 0

# 짝수 번째 인덱스에 들어있는 수들의 합과 3의 배수 번째 인덱스에 들어있는 수들의 평균을 구합니다.
for i in range(10):
	if (i + 1) % 2 == 0:
		sum2 += arr[i]
	if (i + 1) % 3 == 0:
		sum3 += arr[i]
		cnt += 1

# 3의 배수 번째 인덱스에 들어있는 수들의 평균 구하기
avg3 = sum3 / cnt

print(f"{sum2} {avg3:.1f}")