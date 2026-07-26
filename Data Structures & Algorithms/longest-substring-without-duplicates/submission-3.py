class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        new_set = set()
        res = 0
        
        for r in range(len(s)):
            while s[r] in new_set:
                new_set.remove(s[l])
                l += 1
        
            # Keep adding right pointer character
            new_set.add(s[r])
            res = max(res, r - l + 1)
        
        return res
