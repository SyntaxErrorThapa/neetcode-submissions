class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointer approach 
        # First thing, we need to trace the outline of the constainer -- remove white boxes.
        # Initiate two pointers 
        # Water level is determined based on shortest wall
        # If left has shorter wall right wall can not help us. 
        # So we move 
        res = 0
        l = 0 
        r = len(height) - 1
        l_highest = 0
        r_highest = 0

        while l < r:
            if height[l] < height[r]:
                l_highest = max(l_highest, height[l])
                res += l_highest - height[l]
                l += 1
            else:
                r_highest = max(r_highest, height[r])
                res += r_highest - height[r]
                r -= 1

        return res
        
