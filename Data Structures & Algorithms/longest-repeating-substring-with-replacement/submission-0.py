class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Two pointer approach 
        # Condition to check: Find the max count inside dictionary and substract it with sliding window size
        l = 0
        dic = {}
        res = 0
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
            max_counts = 0
            for value in dic.values():
                max_counts = max(max_counts, value)

            while ((i - l + 1) - max_counts) > k:
                dic[s[l]] -= 1
                l += 1
            
            res = max(res, i - l + 1)

        return res