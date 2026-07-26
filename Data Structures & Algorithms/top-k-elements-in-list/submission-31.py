class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the frequency 
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

        # Create bucket
        bucket = [[] for _ in range(len(nums) + 1)]

        # Add frequency to the bucket 
        for key, frequency in dic.items():
            bucket[frequency].append(key)

        # Add the top k frequency
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res 