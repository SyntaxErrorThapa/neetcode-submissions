class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Point to notice is its sorted
        l = 0 
        r = len(numbers) - 1

        while l < r:
            added = numbers[r] + numbers[l]

            if added < target:
                l += 1
            elif added > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        
