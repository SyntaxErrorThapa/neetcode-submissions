class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(cur):
            # Base Case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return 
            
            for num in nums:   
                # Need a checker to check if duplicates
                if num in cur:
                    pass         
                else:
                    cur.append(num)
                    helper(cur)
                    cur.pop()

        helper([])
        return res