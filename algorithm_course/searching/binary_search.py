"""
    Good old binary search...
    Note that the cost for slicing is O(K), so re-writing this so that only the idx val is sent and the array isn't
    sliced is a good idea, but whatevs.
"""

def binary_search(arr, item):
    if not arr:
        return False

    midpoint = len(arr) // 2

    if arr[midpoint] == item:
        return True

    elif arr[midpoint] > item:
        binary_search(arr[:midpoint], item)

    return binary_search(arr[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
assert binary_search(testlist, 3) is False
assert binary_search(testlist, 13) is True
