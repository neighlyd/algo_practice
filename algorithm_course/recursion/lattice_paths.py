"""
    Find the number of paths from the top right to bottom left dots in a lattice matrix.
    https://bradfieldcs.com/algos/recursion/dynamic-programming/
"""


def num_paths(height, width):
    if height == 0 or width == 0:
        # we're dealing with a straight line.
        return 1
    return num_paths(height, width - 1) + num_paths(height - 1, width)


def num_paths_dp(height, width):
    memo = [[1] * (width + 1) for _ in range(0, height + 1)]
    for i, row in enumerate(memo):
        for j, _ in enumerate(row):
            if i == 0 or j == 0:
                continue
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo[-1][-1]