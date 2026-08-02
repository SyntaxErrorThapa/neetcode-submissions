class Solution:
    def trap(self, height: List[int]) -> int:
        # Comparision of heights
        l = 0 
        r = len(height) - 1
        l_highest = 0
        r_highest = 0
        res = 0

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