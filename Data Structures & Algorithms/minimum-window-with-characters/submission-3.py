class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Keep track of formed and required 
        # While loop condition runs until formed == required, check the window size
        # If minimum update the size and string 
        # Remove the left pointer character from dic

        dic_t = {}
        for c in t:
            dic_t[c] = dic_t.get(c, 0) + 1

        formed = 0
        required = len(dic_t)

        min_len = float('inf')
        min_string = ""
        dic_s = {}
        l = 0

        for r in range(len(s)):
            dic_s[s[r]] = dic_s.get(s[r], 0) + 1

            if s[r] in dic_t and dic_s[s[r]] == dic_t[s[r]]:
                formed += 1
            
            while formed == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1 
                    min_string = s[l:r+1]
                
                dic_s[s[l]] -= 1
                if s[l] in dic_t and dic_s[s[l]] < dic_t[s[l]]:
                    formed -= 1
                l += 1
            
        return min_string