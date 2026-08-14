# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(p, q):
            if p is None and q is None:
                return True
            elif p is None and q is not None:
                return False
            elif p is not None and q is None:
                return False 
            elif p is not None and q is not None and p.val != q.val:
                return False
            else:
                result_left = helper(p.left, q.left)
                result_right = helper(p.right, q.right)

                return result_left and result_right 
        
        return helper(p, q)