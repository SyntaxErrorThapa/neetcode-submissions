class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl",
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        bucket = []

        def helper(index):
            # Base Case
            if len(bucket) == len(digits):
                res.append("".join(bucket))
                return
            
            for i in dic[digits[index]]:
                bucket.append(i)
                helper(index + 1)
                bucket.pop()

        if digits:
            helper(0)
        return res