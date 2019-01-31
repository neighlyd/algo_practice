test_arr = [1, -3, 2, 1, -1]

memo = {}


def max_sub_array(arr):
    if len(arr) <= 0:
        return None

    max_global = max_curr = arr[0]

    for i in range(1, len(arr)):
        max_curr = max(arr[i], max_curr + arr[i])
        max_global = max(max_global, max_curr)

    return max_global
