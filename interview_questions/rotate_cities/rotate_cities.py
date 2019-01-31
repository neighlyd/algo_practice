"""
Given an array of words, place words in separate lists if you can rotate the letters of each word (i.e. first goes to
last in sequential order) to form the other words in said list.

in = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris']

out = [
    [ 'Tokyo', 'Kyoto' ],
    [ 'London', 'Donlon' ],
    [ 'Rome' ],
    [ 'Paris' ]
]

"""

# Q1: Can these be anagrams or do the letters simply cycle?
# A: they simply cycle.

# Q2: Does capitalization matter?
# A: The first letter will be the only capitalized word ever.

from collections import defaultdict


def rotate_cities(cities):
    cities_sorted = defaultdict(list)
    for idx, city in enumerate(cities):
        n = sorted(sorted(city.lower()))
        cities_sorted[''.join(n)].append(idx)

    res = []
    for city_list in cities_sorted.values():
        n = []
        for city_idx in city_list:
            n.append(cities[city_idx])
        res.append(n)
    print(res)


rotate_cities(['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris'])