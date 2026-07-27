class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        # Find the start point 
        for num in nums:
            if num - 1 not in s: # Num is our start point
                length = 1
                while num + length in s:
                    length += 1
                res = max(res, length)

        return res
