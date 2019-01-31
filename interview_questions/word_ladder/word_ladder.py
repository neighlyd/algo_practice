"""
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end
such that only one letter can be changed at a time and each intermediate word must exist in the dictionary.
For example, given:

start = 'hit'
end = 'cog'
dict = ['hot','dot','dog','lot','log']

We use a Breadth-First Search to find the shortest path between the start and end point.

For an annotated version of this, see .algorithm_course.graphs.word_ladder.py

"""
from collections import defaultdict, deque
from itertools import product


def build_graph(words):
    """
        Build a graph dictionary mapping nodes to other nodes through a key: set() dictionary.
    :param words: List of Strings - representing the words we want to add to the graph.
    :return: A graph object (dictionary)
    """
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

    # add vertices and edges for words in the same bucket
    for bucket, mutual_neighbors in buckets.items():
        for word1, word2 in product(mutual_neighbors, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph


def traverse(graph, starting_vertex):
    """
        Perform a BFS traversal on an unweighted Digraph from a starting vertex, yielding the current vertex and path
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
