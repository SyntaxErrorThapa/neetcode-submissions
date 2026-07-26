class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i in range(len(nums)):
            sub = target - nums[i]
            
            if sub in dic:
                return [dic[sub], i]
            
            dic[nums[i]] = i

        return []