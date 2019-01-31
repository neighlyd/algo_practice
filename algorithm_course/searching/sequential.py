"""
    just walk down that shit and find what you're looking for. O(n) obvs.
"""


def sequential_search(arr, item):

    for i in arr:
        if i == item:
            return True

    return False


def ordered_sequential_search(arr, item):
    """
        Presumes that the array is ordered and gives a small tweak so that the search stops if the array item is of
        greater value - we know we've gone too far and it's worthless looking further.
    """

    for i in arr:
        if i == item:
            return True

        if i > item:
            return False

    return False
