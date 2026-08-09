class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Using Binary Search

        def helper(l, r):
            if l >= r:
                return nums[l]

            mid = l + (r - l) // 2 
            
            if nums[mid] > nums[r]: # WE know the list is rotated
                return helper(mid + 1, r)
            else:
                return helper(l, mid)

        return helper(0, len(nums)-1) 