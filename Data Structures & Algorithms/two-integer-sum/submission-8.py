class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in dic:
                return [dic[res], i]
            else:
                dic[nums[i]] = i
            print(dic)