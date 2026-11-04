class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def helper(rem):
            # Base case 
            if rem == 0:
                return 0 
            if rem < 0:
                return float('inf')
            if rem in mem:
                return mem[rem]
            
            best = float('inf')
            for coin in coins:
                best = min(best, 1 + helper(rem - coin))

            mem[rem] = best
            return best
        
        ans = helper(amount)

        return ans if ans != float("inf") else -1 