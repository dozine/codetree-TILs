n=int(input())
arr=list(map(int,input().split()))

# def selection_sort():
#     for i in range(n-1):
#         min_index=i
#         for k in range(i+1,n):
#             if arr[min_index]>arr[k]:
#                 min_index=k
#         arr[i],arr[min_index]=arr[min_index],arr[i]

def selection_sort():
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

selection_sort()
for elem in arr:
    print(elem,end=" ")