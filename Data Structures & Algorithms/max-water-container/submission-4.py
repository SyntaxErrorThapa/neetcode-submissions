class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Based on area we move the pointer 
        l = 0 
        r = len(heights) - 1
        max_area = 0 

        while r > l:
            cur_area = (r - l) * min(heights[l], heights[r])

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_area = max(cur_area, max_area)

        return max_area
