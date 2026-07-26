class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False 
            
            l = l + 1
            r = r - 1 

        return True

    def alphaNum(self, letter):
        return (ord('A') <= ord(letter) <= ord('Z') or 
                ord('a') <=  ord(letter) <= ord('z') or 
                ord('0') <= ord(letter) <= ord('9'))