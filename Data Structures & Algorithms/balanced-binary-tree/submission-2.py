# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0
        def helper(root):
            if root is None:
                return 0 
            
            left = helper(root.left)
            right = helper(root.right)

            # self.diff = abs(left - right)
            self.diff = max(self.diff, abs(left - right))
            # if diff > 1:
            #     # Return unbalanced
            #     return False 
            # else:
            #     return True
            
            return 1 + max(left, right)
        helper(root)
        return False if self.diff > 1 else True
