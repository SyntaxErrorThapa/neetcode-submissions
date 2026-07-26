class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Simple solution
        l = 0
        res = []
        for r in range(k, len(nums)+1):
            max_in_window = max(nums[l: r])
            print(nums[l:r])
            print(max_in_window)
            # print(r)
            res.append(max_in_window)
            l+=1

        return res