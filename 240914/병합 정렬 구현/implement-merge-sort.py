# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))
merged_arr = [0] * n 


def merge(low, mid, high):
    i, j = low, mid + 1                 # 각 리스트 내의 원소 위치를 잡습니다.
    
    k = low                             # 병합 시 원소를 담을 위치를 유지합니다.
    while i <= mid and j <= high:       # 두 리스트 내의 원소가 아직 남아있다면
        if arr[i] <= arr[j]:            # 첫 번째 리스트 내의 원소가 더 작다면
            merged_arr[k] = arr[i]      # 해당 원소를 옮겨줍니다. 
            k += 1
            i += 1
        else:
            merged_arr[k] = arr[j]      # 그렇지 않다면 두 번째 리스트 내의 원소를 옮겨줍니다.
            k += 1
            j += 1

    while i <= mid:                     # 아직 첫 번째 리스트 내 원소가 남아있다면
        merged_arr[k] = arr[i]          # 남은 원소들을 전부 옮겨줍니다.
        k += 1
        i += 1
    
    while j <= high:                    # 아직 두 번째 리스트 내 원소가 남아있다면
        merged_arr[k] = arr[j]          # 남은 원소들을 전부 옮겨줍니다.
        k += 1
        j += 1
    
    for k in range(low, high + 1):      # 병합된 리스트를 다시
        arr[k] = merged_arr[k]          # 원본 리스트에 옮겨줍니다.


def merge_sort(low, high):
    if low < high:                    # 원소의 개수가 2개 이상인 경우에만 진행
        mid = (low + high) // 2       # 가운데 원소의 위치
        merge_sort(low, mid)          # 왼쪽 부분에 대해 병합정렬 진행
        merge_sort(mid + 1, high)     # 우측 부분에 대해 병합정렬 진행
        merge(low, mid, high)         # 정렬된 두 리스트를 하나로 병합


merge_sort(0, n - 1)

for elem in arr:
    print(elem, end=" ")