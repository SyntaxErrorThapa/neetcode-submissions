class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Keep track of row, column and square
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(0, len(board)): # Row 
            for j in range(0, len(board[i])): # Column
                # Need to figure out row, column
                num = board[i][j]
                if num == '.':
                    pass
                
                elif num not in row[i] and num not in col[j] and num not in square[(i//3, j//3)]:  
                    row[i].add(num)
                    col[j].add(num)
                    square[(i//3, j//3)].add(num)
                else:
                    return False
        return True 