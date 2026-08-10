# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def helper(root):
            # Base Case
            if root is None:
                return 0

            new_l = helper(root.left)
            new_r = helper(root.right)
            max_height = max(new_l,new_r)

            return max_height + 1
        
        return helper(root)