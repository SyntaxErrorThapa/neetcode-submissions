class Solution:
    def isPalindrome(self, s: str) -> bool:
        def checkCharacter(c):
            return ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9')
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            while not checkCharacter(s[r]) and l < r:
                r -= 1
            while not checkCharacter(s[l]) and l < r:
                l += 1
            if s[r].lower() != s[l].lower():
                return False 

            r -= 1
            l += 1

        return True 