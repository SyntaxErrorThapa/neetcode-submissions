class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        check = set()
        rows = len(board)
        columns = len(board[0])

        def dfs(r, c, index):
            # Base Case
            if index == len(word):
                return True
                
            if (0 > r or r >= rows 
                or 0 > c or c >= columns 
                or word[index] != board[r][c]
                or (r, c) in check):
                return False

            check.add((r, c))
            res = (dfs(r - 1, c, index + 1) 
                    or dfs(r + 1, c, index + 1) 
                    or dfs(r, c + 1, index + 1) 
                    or dfs(r, c - 1, index + 1)) 
            
            check.remove((r, c))
            return res
        
        for i in range(len(board)): # Row
            for j in range(len(board[0])): # Column
                if dfs(i, j, 0):
                    return True
        
        return False 