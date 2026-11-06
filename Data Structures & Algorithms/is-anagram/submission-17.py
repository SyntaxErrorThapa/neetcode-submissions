class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both the string and do it
        # Add both of them in its separate dic 
        
        dic_s = {}
        dic_t = {}

        for ch in s:
            dic_s[ch] = dic_s.get(ch, 0) + 1
        
        for ch in t:
            dic_t[ch] = dic_t.get(ch, 0) + 1
        
        return dic_s == dic_t