from collections import defaultdict


MOVE_OFFSETS = (
    (-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)
)


def legal_moves_from(row, col, board_size):
    """
        Generator to yield all valid variations of a knight's 8 possible moves from any position.
    :param row: Coordinates of starting row
    :param col: Coordinates of starting col
    :param board_size: size of board
    :return: Yield Tuple containing any of the 8 valid end moves.
    """
    # iterate through the possible landing positions for a knight.
    for row_offset, col_offset in MOVE_OFFSETS:
        # calculate where they would end up.
        move_row, move_col = row + row_offset, col + col_offset
        # If they are still on the board, yield that new position.
        if 0 <= move_row < board_size and 0 <= move_col < board_size:
            yield move_row, move_col


def add_vertex(graph, v1, v2):
    # add unweighted, bi-directional nodes to a graph.
    graph[v1].add(v2)
    graph[v2].add(v1)


def build_graph(board_size):
    graph = defaultdict(set)

    # N^2 algo to cycle through and generate all the possible landing spots for a knight from any given position on a
    # board of a given size.
    for row in range(board_size):
        for col in range(board_size):
            for to_row, to_col in legal_moves_from(row, col, board_size):
                add_vertex(graph, (row, col), (to_row, to_col))

    return graph


def first_true(sequence):
    for item in sequence:
        if item:
            return item
    return None


def find_solution_for(board_size, heuristic=lambda graph: None):
    graph = build_graph(board_size)
    total_squares = board_size*board_size

    def traverse(path, current_vertex):
        if len(path) + 1 == total_squares:
            # including the current square, we've visited every square, so return path as solution
            return path + [current_vertex]

        # find children of current_vertex we haven't visited yet, since we want to find a path that touches each square
        # only once.
        yet_to_visit = graph[current_vertex] - set(path)
        if not yet_to_visit:
            # no unvisited neighbors, so dead end
            return None

        # try all valid paths from this vertex
        next_vertices = sorted(yet_to_visit, key=heuristic(graph))
        return first_true(traverse(path + [current_vertex], vertex) for vertex in next_vertices)

    # try to find a solution from any square on the board
    return first_true(traverse([], starting_vertex) for starting_vertex in graph)


def warnsdorff_heuristic(graph):
    """
        This is supposed to reduce the amount of DFS we do, to keep it managaeable.
        DOES NOT WORK IN CURRENT IMPLEMENTATION.
    :param graph:
    :return:
    """
    # Given a graph, returns a comparator function that prioritizes nodes with the fewest subsequent moves.
    def comparator(a, b):
        return len(graph[a]) - len(graph[b])

    return comparator

print(find_solution_for(8, warnsdorff_heuristic))

arr = [
    [0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]
]