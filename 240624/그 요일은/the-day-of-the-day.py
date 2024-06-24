m1, d1, m2, d2 = tuple(map(int, input().split()))
A = str(input())

def count(m, d):
    num_of_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = sum(num_of_day[:m]) + d
    return total_day

total_days = count(m2, d2) - count(m1, d1) + 1
arr = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

start_index = arr.index(A)
cnt = total_days // 7

remaining_days = total_days % 7
for i in range(remaining_days):
    if arr[(start_index + i) % 7] == A:
        cnt += 1

print(cnt)