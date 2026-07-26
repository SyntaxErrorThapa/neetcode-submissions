class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create set 
        dic = set()
        res_len = 0
        l = 0

        for r in range(len(s)):
            while s[r] in dic:
                dic.remove(s[l])
                l += 1     
            dic.add(s[r])
            res_len = max(res_len, r - l + 1)
            
        return res_len
