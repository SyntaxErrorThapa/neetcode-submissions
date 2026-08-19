class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def helper(index, cur, total):
            # Base Case
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or index >= len(nums):
                return

            cur.append(nums[index])
            helper(index, cur, total + nums[index])
            cur.pop()
            helper(index + 1, cur, total)

        helper(0, [], 0)
        return res