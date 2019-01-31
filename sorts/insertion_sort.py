def insertion_sort(arr, rev=False):
    """
        O(n^2)
    :param arr: List
    :param rev: Boolean - reverse sort
    :return: None - sort array in place.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        # insert arr[i] into the sorted sequence arr[1... i-1]
        j = i
        if not rev:
            while j > 0 and arr[j - 1] > key:
                arr[j] = arr[j - 1]
                j = j - 1
        else:
            while j > 0 and arr[j-1] < key:
                arr[j] = arr[j-1]
                j = j - 1
        arr[j] = key


def insertion_sort_recur(arr, n):
    if n <= 1:
        return

    insertion_sort_recur(arr, n-1)

    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last


arr = [5, 2, 4, 6, 1, 3]
res = [1, 2, 3, 4, 5, 6]
res_r = [6, 5, 4, 3, 2, 1]

arr_c = arr[:]
insertion_sort(arr_c)
assert arr_c == res

arr_c = arr[:]
insertion_sort(arr_c, True)
assert arr_c == res_r

arr_c = arr[:]
insertion_sort_recur(arr_c, len(arr_c))
assert arr_c == res
