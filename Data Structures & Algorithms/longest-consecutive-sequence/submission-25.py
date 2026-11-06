class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for i in range(len(nums)):
            # Find the largest consecutive number
            if nums[i] - 1 not in s:

                count = 1
                while nums[i] + count in s:
                    count += 1
                res = max(count, res)
        
        return res