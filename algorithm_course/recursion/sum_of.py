def sum_of(nums):
    if len(nums) == 0:
        return 0

    return nums[0] + sum_of(nums[1:])


print(sum_of([1, 3, 5, 7, 9]))
