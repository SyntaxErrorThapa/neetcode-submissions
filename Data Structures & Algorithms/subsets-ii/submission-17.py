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
                
            subset.append(nums[index])
            helper(index + 1)
            subset.pop()
            # helper(index + 1)
            skip = index
            while skip + 1 < len(nums) and nums[skip + 1] == nums[skip]:
                skip += 1
            helper(skip + 1)
            

        helper(0)
        return res