class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        def rob_lines(start, end):
            mem = {}

            def helper(i):
                # Base Case
                if i > end:
                    return 0
                
                if i in mem:
                    return mem[i]

                mem[i] = max(nums[i] + helper(i + 2), helper(i + 1))
                return mem[i] 
            
            return helper(start)
        
        n = len(nums)
        return max(rob_lines(0,n - 2), rob_lines(1, n - 1))