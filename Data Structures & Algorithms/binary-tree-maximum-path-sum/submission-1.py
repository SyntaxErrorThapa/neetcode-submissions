# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        def helper(root):
            # Base case
            if root is None:
                return 0
            
            left = max(0, helper(root.left)) # To avoid -ve
            right = max(0,helper(root.right))
            
            # path that peaks at this node (can use both sides)
            self.res = max(self.res, left + right + root.val) 
            
            # what we hand to the parent (one side only)
            return root.val + max(left, right)
        
        helper(root)
        
        return self.res