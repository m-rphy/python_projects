# Given an NxN board of letters and a string
#  return true or false if the word can be
#  constructed by only moving horizontally or
#  vertically within the board

board = [
    ["a", "b", "c", "d"],
    ["e", "f", "h", "i"],
    ["j", "k", "l", "m"],
    ["n", "o", "p", "q"],
    ["r", "s", "t", "u"],
]


def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    #  this will hold onto the previously visited node
    path = set()

    # // backtracking for depth first search
    def dfs(r, c, i):
        #  base case
        if i == len(word):
            return True
        # boundry of false conditions
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or board[r][c] != word[i]
            or (r, c) in path
        ):
            return False

        path.add((r, c))
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )

        path.remove((r, c))
        return res

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False

#  O(n * m * 4^n)

print(wordSearch(board, "abc"))
