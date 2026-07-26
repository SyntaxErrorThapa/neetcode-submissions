class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(N^2) algorithm
        
        # new_list = []
        # for i in range(0, len(nums)):
        #     multiple = 1
        #     for j in range(0, len(nums)):
        #         if i == j:
        #             continue 

        #         else:
        #             multiple *= nums[j]
        #     new_list.append(multiple)
        
        # return new_list

        # O(N) algorithm Prefix and Postfix solution
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res