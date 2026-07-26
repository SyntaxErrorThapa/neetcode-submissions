class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        def helper(l, r):
            mid = (l + r) // 2
            if l > r:
                return -1

            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                return helper(l, mid -1)
            else:
                return helper(mid + 1, r)

        return helper(l, r)