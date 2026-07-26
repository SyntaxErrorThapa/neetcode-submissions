class Solution:
    def trap(self, height: List[int]) -> int:
        # Using prefix and postfix approach 
        prefix = [0] * len(height)
        postfix = [0] * len(height)
        
        prefix[0] = height[0]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i])

        postfix[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            postfix[i] = max(postfix[i+1], height[i])

        res = 0
        for i in range(len(height)):
            res += (min(prefix[i], postfix[i]) - height[i])

        return res