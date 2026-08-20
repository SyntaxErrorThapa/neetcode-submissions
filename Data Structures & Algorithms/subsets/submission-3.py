class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def helper(index):
            # Base Case
            if index >= len(nums):
                res.append(subset.copy())
                return

            if index < len(nums):
                res.append(subset.copy()) 
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                helper(i + 1)
                subset.pop()
                
        helper(0)

        return res