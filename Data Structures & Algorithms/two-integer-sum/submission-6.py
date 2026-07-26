class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} # Value -> Index

        for i, val in enumerate(nums):
            diff = target - val 
            
            if diff in dic:
                return [dic[diff], i]

            dic[val] = i