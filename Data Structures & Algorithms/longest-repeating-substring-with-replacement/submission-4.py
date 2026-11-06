class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        res = 0
        maxfreq = 0
        l = 0

        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            maxfreq = max(maxfreq, dic[s[r]])

            # Condition to shrink the window
            while ( r - l + 1 ) - maxfreq > k:
                dic[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res