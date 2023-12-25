n = int(input())
	
# n*n모양 구구단을 출력합니다.
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(f"{i} * {j} = {i * j}", end="")
		if j != n:
			print(",", end=" ")
	print()