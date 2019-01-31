def radix_sort(arr, b=10):
    # get the length of the longest number. This will tell us how many times we need to push the array through the sort
    num_len = len(str(max(arr)))
    n = 0

    while num_len > n:
        # make buckets for every base we're using (e.g. 2 buckets if using base 2, 10 for 10, etc.)
        buckets = [[] for i in range(b)]
        # loop through our array and drop elements into their appropriate bucket for our given loop.
        # For example, on base 10:
        #   1st loop = (i // 1 % 10)
        # If our base is 10, this will drop the number into the bucket based on the last digit.
        for i in arr:
            buckets[i // (b ** n) % b].append(i)
        temp_arr = []
        # use count sort to move from buckets into a temporary list.
        for i in range(len(buckets)):
            temp_arr.extend(buckets[i])
        # add sorted list back to original list
        for i in range(len(temp_arr)):
            arr[i] = temp_arr[i]
        n += 1


mylist = [1, 3, 50, 1, 3, 12351, 16]
radix_sort(mylist, 10)
print(mylist)

