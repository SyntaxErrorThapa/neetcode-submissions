class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(0, len(nums)):
            
            sub = target - nums[i]
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[sub] = i