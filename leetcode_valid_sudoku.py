# ❓ QUESTION:
# Given a 9x9 Sudoku board, determine if it is valid.
# A Sudoku board is valid if:
# - Each row contains the digits 1-9 without repetition.
# - Each column contains the digits 1-9 without repetition.
# - Each of the 9 3x3 sub-boxes contains the digits 1-9 without repetition.
# Empty cells are filled with "." and should be ignored in validation.

# ✅ APPROACH 1: Using defaultdict(set) to track seen digits in rows, columns, and 3x3 boxes
from collections import defaultdict

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

row = defaultdict(set) 
col = defaultdict(set) 
square = defaultdict(set)  # Key = (row//3, col//3)

for r in range(9): 
    for c in range(9): 
        val = board[r][c]
        if val == ".": 
            continue 
        if val in row[r] or val in col[c] or val in square[(r//3, c//3)]: 
            print(False)
        row[r].add(val) 
        col[c].add(val) 
        square[(r//3, c//3)].add(val)

# ✅ APPROACH 2: Object-oriented design using helper functions to validate rows, columns, and subgrids
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        This method checks rows, columns, and 3x3 subgrids using helper methods.
        """
        return self.isRowValid(board) and self.isColValid(board) and self.isSubValid(board)

    def isRowValid(self, board):
        # Check that each row contains unique digits (excluding '.')
        for row in board:
            if not self.isUnitValid(row):
                return False
        return True

    def isColValid(self, board):
        # Transpose the board using zip(*board) to iterate through columns
        for col in zip(*board):
            if not self.isUnitValid(col):
                return False
        return True
    
    def isSubValid(self, board):
        # Loop through each 3x3 subgrid using top-left anchors (0,3,6)
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                sub_grid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isUnitValid(sub_grid):
                    return False
        return True
    
    def isUnitValid(self, units):
        # Remove '.' and check if all elements are unique
        unit = [i for i in units if i != '.']
        return len(set(unit)) == len(unit)
