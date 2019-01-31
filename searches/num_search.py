"""
    Using loop invariants, search an array for numbers.
    X is loop invariant, because it is False before the loop initiates and its value does not depend upon the loop
    itself.
"""
def num_search(nums, search):
    x = False
    for i in range(len(nums)):
        if nums[i] == search:
            x = True
    return x

arr1 = [5, 2, 4, 6, 1, 3]
print(num_search(arr1, 6))
print(num_search(arr1, 20))
