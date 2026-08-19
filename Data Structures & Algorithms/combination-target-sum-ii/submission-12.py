class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(i, cur, total):
            # Base Case 
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                # Prune 
                if candidates[j] + total > target:
                    break
                
                cur.append(candidates[j])
                helper(j + 1, cur, total + candidates[j])
                cur.pop()

        helper(0, [], 0)
        return res
