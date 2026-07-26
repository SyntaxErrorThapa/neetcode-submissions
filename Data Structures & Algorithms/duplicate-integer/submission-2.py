class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use of hash map 

        dic = {}

        for i in nums:
            if i in dic:
                return True 
            dic[i] = 1
        return False