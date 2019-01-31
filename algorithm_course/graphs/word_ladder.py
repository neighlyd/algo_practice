from collections import defaultdict, deque
from itertools import product


def create_graph(words):
    """
        Build a graph dictionary mapping nodes to other nodes through a key: set() dictionary.
    :param words: List of Strings - representing the words we want to add to the graph.
    :return: A graph object (dictionary)
    """
    graph = defaultdict(set)
    buckets = defaultdict(list)

    for word in words:
        for i in range(len(word)):
            # note that when i + 1 overruns we won't get an index error because slicing doesn't return an IndexError, it
            # just gives nothing back in that instance.
            bucket = '{}_{}'.format(word[:i], word[i + 1:])
            buckets[bucket].append(word)

    for bucket, mutual_neighbors in buckets.items():
        for word1, word2 in product(mutual_neighbors, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph


def breadth_first_search(graph, starting_vertex, goal):

    # If the starting and ending are the same, just return a single jump list.
    if starting_vertex == goal:
        return [starting_vertex]

    # keep a set of all vertices we have visited.
    visited = {starting_vertex}

    # Our visitation queue will be a list of lists representing various paths through the graph.
    # We will use a deque because we will be removing from the left and appending to the right.
    # A deque will allow us to keep this at O(1) time.
    queue = deque([[starting_vertex]])

    while queue:
        # Remove the left-most path in our queue. This is the longest-waiting in the queue
        # (I'm sure there's a term for this).
        path = queue.popleft()
        # Because this represents a path from start -> current, we only need to look at the very last element of this
        # list. It represents the node we want to start from (i.e. the deepest node in the search).
        vertex = path[-1]

        # If we've found our goal, great. Return the current path we've popped out. That's an optimal route there.
        if vertex == goal:
            return path

        # If not, retrieve the neighboring routes for this vertex, ignoring any that are in our visited set.
        for neighbor in graph[vertex] - visited:
            # Add all of its neighbors to our visited set, so we know that we have 'touched' them (and queued them up
            # for examination).
            visited.add(neighbor)
            # take the current path and add this neighbor to the end of it, then add that new list to the end of the
            # queue to await examination. Once it is popped off (at the beginning of the while loop), it will check this
            # neighbor node to see if it is our goal.
            # We don't want to check to see if the neighbor/child is goal here, because one of its actual neighbors (not
            # children; i.e. one in the for loop above) may be a more optimal solution. So we defer checking until the
            # next iteration of the while loop.
            queue.append(path + [neighbor])


def breadth_first_search_recurse(graph, start, goal, q=None, visited=None):
    if q is None:
        q = deque([[start]])
        visited = {start}

    if len(q) == 0:
        return None

    path = q.popleft()
    vertex = path[-1]

    if vertex == goal:
        return path

    for neighbor in graph[vertex] - visited:
        visited.add(neighbor)
        q.append(path + [neighbor])
    return breadth_first_search_recurse(graph, start, goal, q, visited)


arr = ['FOOL', 'WOOL', 'COOL', 'POOL', 'POLL', 'POLE', 'PALE', 'SALE', 'SAGE']
g = create_graph(arr)
print(breadth_first_search(g, 'FOOL', 'SAGE'))