"""
    Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.
"""


def zero_matrix(m):
    rows = set()
    cols = set()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in rows:
        for j in range(len(m[i])):
            m[i][j] = 0
    for j in cols:
        for i in range(len(m)):
            m[i][j] = 0


matrix = [[0, 1, 2], [3, 6, 4], [5, 0, 7]]


zero_matrix(matrix)
print(matrix)

m2 = [[1, 2], [3, 4]]

zero_matrix(m2)
print(m2)