# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Use BFS and always add the furtheset right 
        stack = []
        res = []
        stack.append(root)

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
                res.append(temp[-1])
            
        return res