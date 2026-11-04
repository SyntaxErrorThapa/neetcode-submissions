class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0] * (n + 1)
        mem[n], mem[n-1] = 1, 1

        for i in range(n-2, -1, -1):
            mem[i] = mem[i+1] + mem[i+2]
        
        return mem[0]