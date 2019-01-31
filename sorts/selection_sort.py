def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr1 = [5, 2, 4, 6, 1, 3]
print(arr1)
selection_sort(arr1)
print(arr1)