import math as m
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.final_res = float("inf")
        max_pace = max(piles)

        def helper(l, r):
            if l > r:
                return self.final_res

            mid = l + (r - l) // 2
            res = 0

            for i in range(len(piles)):
                res += m.ceil(piles[i] / mid)

            if res <= h:
                self.final_res = min(self.final_res, mid)

                return helper(l, mid - 1)

            else:
                return helper(mid + 1, r)

        return helper(1, max_pace)