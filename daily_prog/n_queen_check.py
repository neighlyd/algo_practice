"""
For the purpose of this challenge, the N queens problem consists of putting one queen on every column (labeled a, b, c, ...) of an NxN chessboard, such that no two queens are in the same row or diagonal. An example valid solution for N = 6 is:

6  . . Q . . .
5  . . . . . Q
4  . Q . . . .
3  . . . . Q .
2  Q . . . . .
1  . . . Q . .
   a b c d e f
In chess notation, the squares with queens in this solution are called a2, b4, c6, d1, e3, and f5. We'll represent solutions by listing the rows that each column's queen appears in from left to right, so this solution is represented as the array {2, 4, 6, 1, 3, 5}.


Challenge
Given an array of 8 integers between 1 and 8, determine whether it represents a valid 8 queens solution.

qcheck({4, 2, 7, 3, 6, 8, 5, 1}) => true
qcheck({2, 5, 7, 4, 1, 8, 6, 3}) => true
qcheck({5, 3, 1, 4, 2, 8, 6, 3}) => false   (b3 and h3 are on the same row)
qcheck({5, 8, 2, 4, 7, 1, 3, 6}) => false   (b8 and g3 are on the same diagonal)
qcheck({4, 3, 1, 8, 1, 3, 5, 2}) => false   (multiple problems)
You may optionally handle solutions for any N, not just N = 8.
"""


def check_row(arr):
    """
        Check to see if any two elements are on the same row (Defined as having the same number).
    :param arr: List[ints]
    :return: Boolean
    """
    # Put array into a set and check to see if the result is same length as starting array, if not there are repeats
    # (i.e. at least two queens are on the same row).
    return len(arr) == len(set(arr))


def check_diagonal(arr):
    """
        Checks if any queen position in the array intersects diagonally with another queen position.
    :param arr: List[ints] of queen positions.
    :return: (Tuple: i,j) of intersecting diagonal queen positions or None.
    """
    # iterate through array, then iterate through all elements to the right of that element checking diagonal as you
    # proceed. Diagonal is found by adding/subtracting 1 for each step we take. This is done through a counter.
    # There may be a better solution which carries each element forward, but I can't figure it.
    for i in range(len(arr)):
        diag_counter = 1
        for j in range(i + 1, len(arr)):
            if arr[i] + diag_counter == arr[j] or arr[i] - diag_counter == arr[j]:
                return i, j
            diag_counter += 1


def fix_diagonal(arr, d_queens):
    """
        Taking the original array and the location of intersecting diagonals, swap positions between conflicting and
        non-conflicting points until we either get one that works or we reach the end and find nothing.
    :param arr: List[ints] of queen positions.
    :param d_queens: (Tuple: i,j) position of diagonal intersecting queen positions.
    :return: List[ints] with new locations for intersecting queens or None if no new positions found.
    """
    q_1 = d_queens[0]
    q_2 = d_queens[1]
    temp_arr = arr[:]
    for i in range(len(temp_arr)):
        if temp_arr[i] != temp_arr[q_1] or temp_arr[i] != temp_arr[q_2]:
            temp_arr[q_1], temp_arr[i] = temp_arr[i], temp_arr[q_1]
            if qcheck(temp_arr):
                return temp_arr
            temp_arr[i], temp_arr[q_1] = temp_arr[q_1], temp_arr[i]
    for i in range(q_2 + 1, len(temp_arr)):
        temp_arr[q_2], temp_arr[i] = temp_arr[i], temp_arr[q_2]
        if qcheck(temp_arr):
            return temp_arr
        temp_arr[i], temp_arr[q_2] = temp_arr[q_2], temp_arr[i]
    return None


def qcheck(arr, check=False):
    """
        Check a list of queen positions to see if they are on the same row or diagonal as each other.
        Accepts optional `check` param, which will attempt to fix diagonal intersections.
    :param arr: List[ints] of queen positions
    :param check: Boolean: should we attempt to fix conflicting diagonal intersections? Defaults to False
    :return: List[ints] of correct queen positions if exist, False if none exist
    """
    # Will only return True if both check_row and check_diagonal return True.
    c_d = check_diagonal(arr)
    if check_row(arr) and c_d is None:
        return arr
    if c_d and check is True:
        return fix_diagonal(arr, c_d) or False
    return False


assert qcheck([4, 2, 7, 3, 6, 8, 5, 1]) == [4, 2, 7, 3, 6, 8, 5, 1]
assert qcheck([2, 5, 7, 4, 1, 8, 6, 3]) == [2, 5, 7, 4, 1, 8, 6, 3]
assert qcheck([5, 3, 1, 4, 2, 8, 6, 3]) is False
assert qcheck([5, 8, 2, 4, 7, 1, 3, 6]) is False
assert qcheck([4, 3, 1, 8, 1, 3, 5, 2]) is False

assert qcheck([8, 6, 4, 2, 7, 1, 3, 5], True) == [4, 6, 8, 2, 7, 1, 3, 5]
assert qcheck([8, 5, 1, 3, 6, 2, 7, 4], True) == [8, 4, 1, 3, 6, 2, 7, 5]
assert qcheck([4, 6, 8, 3, 1, 2, 5, 7], True) == [4, 6, 8, 3, 1, 7, 5, 2]
assert qcheck([7, 1, 3, 6, 8, 5, 2, 4], True) == [7, 3, 1, 6, 8, 5, 2, 4]
