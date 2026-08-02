class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy while its min and sell when its high
        l = 0
        total = 0
        
        for r in range(len(prices)):
            new_total = prices[r] - prices[l]

            if new_total < 0:
                l = r

            total = max(total, new_total)

        return total
            