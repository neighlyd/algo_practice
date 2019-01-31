def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


arr = [5, 2, 4, 6, 1, 3]
res = [1, 2, 3, 4, 5, 6]
bubble_sort(arr)
assert arr == res