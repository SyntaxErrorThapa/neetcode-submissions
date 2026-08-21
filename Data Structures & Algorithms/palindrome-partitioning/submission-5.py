class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def checkPalidrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False 
            
                l += 1
                r -= 1
            
            return True

        def helper(index):
            # Base Case
            if index >= len(s):
                res.append(subset.copy())    
                return 

            for j in range(index, len(s)):
                if checkPalidrome(s, index, j):
                    subset.append(s[index:j+1])
                    helper(j + 1)
                    subset.pop()
            

        helper(0)
        return res
