class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort it out and check 
        if len(s) != len(t):
            return False 
        return sorted(s) == sorted(t)