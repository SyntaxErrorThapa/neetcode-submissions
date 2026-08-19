class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def helper(i):
            # Base Case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            helper(i + 1)
            subset.pop()
            helper(i + 1)
        
        helper(0)
        return res