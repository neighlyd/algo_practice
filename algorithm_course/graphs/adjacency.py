"""
    One of the easiest ways to store information about a graph is a 2D Matrix, where the column and row headers are the
vertices. Where they align gives us the weight of the connections. If these are Null, then they do not connect. If there
are not many connections, then the adjacency matrix is said to be 'sparse.' A matrix is not an efficient way to store
sparse data.
"""

"""
    A more space-efficient storage mechanism is the adjacency list. In this implementation, we have a Graph object, 
which stores a reference to all of its Node objects. These Node objects then have a reference to the Node objects that 
they connect to. 
"""