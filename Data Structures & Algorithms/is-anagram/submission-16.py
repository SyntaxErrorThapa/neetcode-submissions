class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        dic_a = {}
        dic_b = {}

        for a in s:
            dic_a[a] = 1 + dic_a.get(a, 0)
        
        for b in t:
            dic_b[b] = 1 + dic_b.get(b, 0)

        return dic_a == dic_b