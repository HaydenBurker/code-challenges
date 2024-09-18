# Create a function that takes in an adjacency matrix and two nodes then checks if two nodes are adjacent in an undirected graph

def is_adjacent(matrix, n1, n2):
    return matrix[n1][n2] == 1

matrix = [
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 0]
]

print(is_adjacent(matrix, 0, 1)) # true
print(is_adjacent(matrix, 2, 1)) # false
print(is_adjacent(matrix, 1, 0)) # true

matrix = [
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0]
]

print(is_adjacent(matrix, 4, 3)) # false
print(is_adjacent(matrix, 0, 4)) # true
print(is_adjacent(matrix, 1, 4)) # false
print(is_adjacent(matrix, 0, 3)) # true