class Solution:
    def climbStairs(self, n: int) -> int:
        
        dic = {}

        def helper(i):
            # Base Case 
            if i in dic:
                return dic[i]

            if i == n:
                return 1
            
            if i > n:
                return 0
            
            l = helper(i + 1)
            r = helper(i + 2)
            dic[i] = l + r
            return l + r

        
        return helper(0)