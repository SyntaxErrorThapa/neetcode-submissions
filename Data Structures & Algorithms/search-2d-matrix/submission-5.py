class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(mat):
            
            mid = len(mat) // 2
            if not mat:
                return False 
            if mat[mid] == target:
                return True 
            elif mat[mid] < target:
                # check right 
                return helper(mat[mid + 1:])
            elif mat[mid] > target:
                return helper(mat[:mid]) 

        for i in range(len(matrix)):
            # Check the last index to determine which row contains it?
            if matrix[i][-1] > target:
                # Current row and perform binary search\
                return helper(matrix[i])
            elif matrix[i][-1] == target:
                return True
        return False