class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def helper(cur):
            # Base Case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return 

            for num in nums:
                if num in used:
                    continue

                cur.append(num)
                used.add(num)

                helper(cur)

                cur.pop()
                used.remove(num)

        helper([])
        return res