class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Find the start; num is the start if and only if num - 1 is not present inside the set
        s = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                res = max(res, length)

        return res
