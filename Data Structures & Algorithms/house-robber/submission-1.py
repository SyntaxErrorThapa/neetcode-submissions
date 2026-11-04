class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0

        for x in nums:
            prev, curr = curr, max(prev + x, curr)
        
        return curr