class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # N^2 algorithm 
        
        new_list = []
        for i in range(0, len(nums)):
            multiple = 1
            for j in range(0, len(nums)):
                if i == j:
                    continue 

                else:
                    multiple *= nums[j]
            new_list.append(multiple)
        
        return new_list