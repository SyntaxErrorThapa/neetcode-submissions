class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top_left = False

        for i in range(0, len(matrix)): # row 
            for j in range(0, len(matrix[0])):
                # If there is zero, check the row and column 
                # Update the first row and column
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0: # For row > 0
                        matrix[i][0] = 0
                    else: # Check for the overlap cell
                        top_left = True 
        
        # Zeroing the row and column
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Zeroing the first row and first column
        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        if top_left:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0