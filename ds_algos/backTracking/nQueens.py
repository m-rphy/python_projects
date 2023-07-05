# N-queens

# we are given n queens and n differnet queens, such that no two queens never attack each other

#  example
# [[0,1,0,0],
#  [0,0,0,1],
#  [1,0,0,0],
#  [0,0,1,0]]

# every queen has to be in a different row and column
# (the hard part is diagonals) Each queen can only be in
#  different diagonals

def nQueens(n):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    # list of solutions
    res = []
    # Board that we are traversing
    board = [["."] * n for i in range(n)]

    #  backtracking function
    def backTrack(r):
        # we've found a solution
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        # Backtrack baby!
        for c in range(n):
            #  check for error conditions
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            #  if passed error conditions
            #  add the next set of error conditions for next back track
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            # recursive case
            backTrack(r + 1)

            #  remove the last error conditions (and queen)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    #  start backtracking
    backTrack(0)
    return res
