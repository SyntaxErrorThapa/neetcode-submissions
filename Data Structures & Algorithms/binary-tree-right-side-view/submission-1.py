# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(root, cur):
            if root is None:
                return
            if len(res) == cur:
                res.append(root.val)
            helper(root.right, cur + 1)
            helper(root.left, cur + 1)
        
        helper(root, 0)
        return res

            