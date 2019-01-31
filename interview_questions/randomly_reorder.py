"""
    Randomly reorder an array in-place.
    Uses a Knuth shuffle algorithm.

    input = [1, 2, 3, 4]
    output = [2, 1, 4, 3] (or whatever)

    given:

    random() => random num 0-1
    floor(x) => highest integer before x (e.g. floor(2.89) => 2)

"""

from random import random
from math import floor


def random_resort(l):
    for i in range(len(arr)-1, 0, -1):
        r = floor(i * random())
        arr[i], arr[r] = arr[r], arr[i]


arr = [1, 2, 3, 4, 5]
print(random_resort([1, 2, 3, 4, 5]))
print(arr)
