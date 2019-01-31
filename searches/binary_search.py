from sorts.merge_sort import merge_sort


def binary_search_recurse(arr, num, left, right):
    """
        Assumes a sorted array.
    :param arr: Array of sorted elements
    :param num: element you wish to find.
    :return: True or False whether element is in list.
    """
    if left > right:
        return False
    mid = left + (right - left)//2
    if arr[mid] == num:
        return True
    elif arr[mid] > num:
        return binary_search_recurse(arr, num, left, mid - 1)
    elif arr[mid] < num:
        return binary_search_recurse(arr, num, mid + 1, right)


def binary_search(arr, num):
    return binary_search_recurse(arr, num, 0, len(arr)-1)


arr1 = [5, 2, 4, 6, 1, 3]
merge_sort(arr1)
print(binary_search(arr1, 6))
print(binary_search(arr1, 20))
print(binary_search(arr1, 4))