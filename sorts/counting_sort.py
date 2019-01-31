"""
    O(n + k) where k is the range of keys we have.
"""

def count_sort_sub_list(arr):
    """
        We can take advantage of a list of lists to do a variant on the count-sort.
    :param arr:
    :return:
    """
    temp_arr = [[] for x in range(max(arr) + 1)]
    for i in range(len(arr)):
        temp_arr[arr[i]].append(arr[i])
    output = []
    for i in range(len(temp_arr)):
        output.extend(temp_arr[i])
    return output


def count_sort_trad(arr):
    """
        THe traditional count sort uses the sums of the number of elements discovered to sort them.
    :param arr:
    :return:
    """
    temp_arr = [0 for x in range(max(arr) + 1)]
    for i in range(len(arr)):
        temp_arr[arr[i]] += 1
    for i in range(1, len(temp_arr)):
        temp_arr[i] += temp_arr[i - 1]
    ret_arr = [None for x in range(len(arr) + 1)]
    for i in range(len(arr) - 1, -1, - 1):
        ret_arr[temp_arr[arr[i]]] = arr[i]
        temp_arr[arr[i]] -= 1
    return ret_arr[1:]

arr = [2, 5, 3, 0, 2, 3, 0, 3]

print(count_sort_trad(arr))
