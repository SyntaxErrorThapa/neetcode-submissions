class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            # Edge case for duplicates 
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                total = nums[l] + nums[i] + nums[r]
                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1
                
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Check for duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return result