class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # The main thing about this question is the numbers are already sorted in non-decreasing order.
        # We can use this to our advantage
        # Two pointer left and right
        # Calculate the sum 
        # If sum is greater move right pointer 
        # Else move left pointer 
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            result = numbers[l] + numbers[r]

            if result > target:
                r -= 1
            elif result < target:
                l += 1
            else:
                return [l + 1, r + 1]
        