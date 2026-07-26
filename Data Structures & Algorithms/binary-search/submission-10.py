class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # look left side 
                return helper(l, mid - 1)
            elif nums[mid] < target:
                return helper(mid + 1, r)
        
        return helper(0, len(nums) - 1)