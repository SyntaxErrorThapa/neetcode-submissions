class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Add character to data structure called set 
        # We move pointer as we add character and remove character from the set 

        store = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            store.add(s[r])
            res = max(res, r - l + 1)

        return res
