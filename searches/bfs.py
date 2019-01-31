"""
    A Breadth-First Search (BFS) builds a search tree by examining each layer of a graph before moving onto the next.
    This differs from a Depth-First Search (DFS), which digs directly down one branch of a graph before branching out
    to others (if the discovered branch is a dead-end/does not fit given criteria).

    To perform a BFS, we take a starting vertex [call this SV] of a graph, place all of its children into a queue
    (made of a list of lists), pop one off [call this V2], then examine its children. If there are any overlaps between
    SV's children and V2's [call this V3], we remove them and append the rest to queue as a list after SV's children.

    The reason we do not add any of V2's children that were also V1's children is because we know the path from SV to V3
    is by necessity shorter than the path between SV -> V2 -> V3.

    We then perform this step as often as possible until we find the ending vertex [call this EV]. At which point we
    return the current path, as it will be the shortest.
"""
from collections import defaultdict, deque
from itertools import product


# One way to build the graph necessary for a BFS is to use a dictionary mapping nodes to a set of children. This method
# does not require creating a unique Graph or Node class. It is therefore much more simple and straight-forward. Though,
# what it has in ease, it lacks in mutability and complexity.
def build_graph(words):
    """
        Build a graph dictionary mapping nodes to other nodes through a key: set() dictionary.
    :param words: List of Strings - representing the words we want to add to the graph.
    :return: A graph object (dictionary)
    """
    # buckets are temporary holding objects for lists of common elements between words.
    buckets = defaultdict(list)

    graph = defaultdict(set)

    for word in words:
        for i in range(len(word)):
            # create a new string with one letter missing from the word. E.G. '_OOL' from 'POOL'
            bucket = '{}_{}'.format(word[:i], word[i + 1:])
            # Create a new (or append to existing) hash entry with that as the key
            # Using the word that derived it as the value added.
            # This gives us the commonality for all words. E.G. {'_OOL': ['POOL', 'FOOL']}
            buckets[bucket].append(word)

    # add vertices and edges for words that are contained in the same holding bucket.
    for bucket, mutual_neighbors in buckets.items():
        for word1, word2 in product(mutual_neighbors, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph


def traverse(graph, starting_vertex):
    """
        Perform a BFS traversal on an unweighted bigraph from a starting vertex, yielding the current vertex and path
        during each loop.
    :param graph: A graph object consisting of a dictionary of a key: set() pair.
    :param starting_vertex: The starting object to look at.
    :return: Yields the current vertex and path so long as there are avenues to explore.
    """
    visited = set()
    queue = deque([[starting_vertex]])
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        yield vertex, path
        for neighbor in graph[vertex] - visited:
            visited.add(neighbor)
            queue.append(path + [neighbor])


# The word_ladder() function uses a BFS to find the shortest route between two words in a list.
def word_ladder(start, end, words):
    """
        Create a word-ladder between the start and end words, using the provided words list.
    :param start: String - the word we want to start from.
    :param end: String - the word we want to end at.
    :param words: List of strings - the words we want to traverse.
    :return: None if no path found or a String in the form of a unidirectional graph; e.g. "hit -> bit -> bot"
    """
    if start not in words:
        words.append(start)
    if end not in words:
        words.append(end)
    g = build_graph(words)

    for vertex, path in traverse(g, start):
        if vertex == end:
            return ' -> '.join(path)
    # By default will return None if no path is found.
