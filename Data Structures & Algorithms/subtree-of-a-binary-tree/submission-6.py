# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(root, subroot):
            if not root and not subroot:
                return True
            
            if not root or not subroot:
                return False 
            
            if root.val != subroot.val:
                return False
            
            root_left = isSame(root.left, subroot.left)
            root_right = isSame(root.right, subroot.right)

            return root_left and root_right

        if root is None:
            return False
        if isSame(root, subRoot):
            return isSame(root, subRoot)
        
        res_val_left = self.isSubtree(root.left, subRoot)
        res_val_right = self.isSubtree(root.right, subRoot)

        return res_val_left or res_val_right