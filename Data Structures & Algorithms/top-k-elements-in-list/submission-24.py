class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive Approach 
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        
        # # Sorting based on decending order 
        # decending = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)[:k])
        
        # return list(decending.keys())

        # Bucket sort 
        result = [[] for i in range(len(nums) + 1)]

        # Count the frequency 
        dic = {}

        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

        # Add the frequency to the result 
        for key, value in dic.items():
            result[value].append(key)
        
        print(result)

        # Now get the required number of large frequency digit 
        res = []
        for i in range(len(result) - 1, 0, -1):
            for value in result[i]:
                res.append(value)
                if len(res) == k:
                    return res
