from collections import defaultdict

simple_graph = {
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': [],
    'D': ['E'],
    'E': ['B', 'F'],
    'F': ['C']
}


def depth_first_search(graph, starting_vertex):
    """
        This explores all branches, creating alternative trees, and returns a value with the order in which leaves were
        discovered and when those branches became final destinations.
        https://bradfieldcs.com/algos/graphs/depth-first-search/
    :param graph:
    :param starting_vertex:
    :return:
    """
    visited = set()
    # for some fuckin' reason, this works if I make counter a list, but not an int.
    # WTF?
    counter = [0]
    traversal_times = defaultdict(dict)

    def traverse(vertex):
        visited.add(vertex)
        counter[0] += 1
        traversal_times[vertex]['discovery'] = counter[0]

        for next_vertex in graph[vertex]:
            if next_vertex not in visited:
                traverse(next_vertex)

        counter[0] += 1
        traversal_times[vertex]['finish'] = counter[0]

    traverse(starting_vertex)
    return traversal_times

print(depth_first_search(simple_graph, 'A'))