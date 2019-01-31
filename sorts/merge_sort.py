def merge_sort(arr):
    if len(arr) > 1:
        # do the splitting
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        # do the recombining
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # catch stragglers
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # catch stragglers
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr1 = [5, 2, 4, 6, 1, 3]
print(arr1)
merge_sort(arr1)
print(arr1)