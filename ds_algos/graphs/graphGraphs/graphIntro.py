#  1 Matrix
#  2 Adjacency Matrix
#  3 Adjacent List
# 
#  NOTE:
#   Vertices are the same as nodes
#   Pointers are Edges

#  Graphs can, and often do, have cycles!
# Edges <= (Vertices)^2

# Directed Graph -> Each pointer has a direction (BST and singlely-LL are directed graphs)

# Undirected Graphs are essentially doubly-LL

#  Matrix (undirected graph)

treasureMap = [[0, 0, 0, 0],
               [1, 1, 'X', 0],
               [1, 0, 0, 1],
               [0, 0, 1, 0]]

teasure = treasureMap[1][2] # row 1 and column 2

#  Adjecency matrix
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0]]


def dfs(grid, r, c, visit = set()):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r,c) < 0 or 
       r == ROWS or c == COLS or
       (r, c) in visit or grid[r][c] == 1):
         return 0
    if r == ROWS - 1 or c == COLS - 1:
          return 1
    
    count = 0
    visit.add((r, c))
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count

print(dfs(grid, 0, 0, set()))