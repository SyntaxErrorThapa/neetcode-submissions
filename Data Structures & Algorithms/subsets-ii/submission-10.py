class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def helper(index):
            # Base Case
            if index >= len(nums):
                res.append(subset.copy())
                return

            if index < len(nums):
                res.append(subset.copy()) 
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                helper(i + 1)
                subset.pop()
                
        helper(0)

        return res