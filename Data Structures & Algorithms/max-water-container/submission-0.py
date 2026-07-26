class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initiate Left pointer and right pointer 
        # Find the minimum between left pointe and right pointer 
        # Find the window between pointers
        # Move the smallest pointer 

        l = 0 
        r = len(heights) - 1
        res = 0 

        while l < r:
            min_height = min(heights[l], heights[r])
            res = max(res, (min_height * (r - l))) 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res