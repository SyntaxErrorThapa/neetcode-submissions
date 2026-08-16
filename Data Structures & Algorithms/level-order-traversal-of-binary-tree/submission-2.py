# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = []
        stack.append(root)
        res = []

        while stack:
            len_stack = len(stack)
            temp = []

            for i in range(len_stack):
                cur = stack.pop(0)
                if cur:
                    temp.append(cur.val)
                    stack.append(cur.left)
                    stack.append(cur.right)
            if temp:
                res.append(temp)
            
        return res