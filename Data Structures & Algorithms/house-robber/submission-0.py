class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def helper(i):
            # Base Case 

            if i >= len(nums):
                return 0

            if i in mem:
                return mem[i]

            mem[i] = max(nums[i] + helper(i + 2), helper(i + 1)) 
            return mem[i]

        return helper(0)