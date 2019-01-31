"""
    Finding an intersection of 3 pre-sorted arrays.

    arr1 = [2, 6, 9, 11, 13, 17]
    arr2 = [3, 6, 7, 10, 13, 18]
    arr3 = [4, 5, 6, 9, 11, 13]

"""


def arr_intersect(arr1, arr2, arr3):
    x = 0
    y = 0
    z = 0
    res = []
    while x < len(arr1) and y < len(arr2) and z < len(arr3):
        if arr1[x] == arr2[y] == arr3[z]:
            res.append(arr1[x])
            x += 1
            y += 1
            z += 1
        elif arr1[x] < arr2[y]:
            x += 1
        elif arr2[y] < arr3[z]:
            y += 1
        else:
            z += 1
    return res


arr1 = [2, 6, 9, 11, 13, 17]
arr2 = [3, 6, 7, 10, 13, 18]
arr3 = [4, 5, 6, 9, 11, 13]

print(arr_intersect(arr1, arr2, arr3))