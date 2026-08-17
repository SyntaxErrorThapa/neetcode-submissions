# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, left, right):
            # Base Case
            if root is None:
                return True 
            if not (left < root.val < right):
                return False
            
            left_val = helper(root.left, left, root.val)
            right_val = helper(root.right, root.val, right)

            return left_val and right_val

        return helper(root, float("-inf"), float("inf"))
