class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(l, r):
            # Base Case
            if l > r:
                return -1

            mid = l + (r - l) // 2

            # Compare mid with right 
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]: # right segment
                    return helper(mid + 1, r)
                else:
                    return helper(l, mid - 1)
            else:
                if nums[l] <= target < nums[mid]: # left segment 
                    return helper(l, mid - 1)
                else:
                    return helper(mid + 1, r)
        
        return helper(0, len(nums) - 1)