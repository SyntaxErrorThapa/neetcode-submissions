class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive Approach 
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        # Sorting based on decending order 
        decending = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)[:k])
        
        return list(decending.keys())
