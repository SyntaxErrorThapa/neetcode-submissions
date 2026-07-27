class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            while not s[r].isalnum() and l < r:
                r -= 1
            while not s[l].isalnum() and l < r:
                l += 1
            if s[r].lower() != s[l].lower():
                return False 

            r -= 1
            l += 1

        return True 