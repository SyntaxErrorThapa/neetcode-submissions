class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        dic_a = {}
        dic_b = {}
        for i in range(len(s1)):
            dic_a[s1[i]] = dic_a.get(s1[i], 0) + 1
            dic_b[s2[i]] = dic_b.get(s2[i], 0) + 1

        if dic_a == dic_b:
            return True 

        l = 0 
        for r in range(len(s1), len(s2)):
            dic_b[s2[r]] = dic_b.get(s2[r], 0) + 1
            dic_b[s2[l]] -= 1

            if dic_b[s2[l]] == 0:
                del dic_b[s2[l]]
            l += 1
            
            if dic_a == dic_b:
                return True 
        return False