# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Pre order traversal
        res = []
        def helper(root):
            # Base case 
            if root is None:
                res.append("N")
                return 
            res.append(str(root.val))
            helper(root.left)
            helper(root.right)
        helper(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def helper():
            # Base Case 
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()