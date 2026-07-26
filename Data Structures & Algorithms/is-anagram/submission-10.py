class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}

        # First check if both have same size 
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = 1
            else:
                dic_s[s[i]] += 1

            if t[i] not in dic_t:
                dic_t[t[i]] = 1
            else:
                dic_t[t[i]] += 1
        
        return dic_s == dic_t