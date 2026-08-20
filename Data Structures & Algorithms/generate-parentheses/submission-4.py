class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def helper(o, c):
            # Base Case
            if o == n and c == n:
                res.append("".join(subset))
                return 
            
            # Recursive Case 
            if o < n:
                subset.append("(")
                helper(o + 1, c)
                subset.pop()
            
            if c < o:
                subset.append(")")
                helper(o, c + 1)
                subset.pop()
            
            
        helper(0, 0)
        return res