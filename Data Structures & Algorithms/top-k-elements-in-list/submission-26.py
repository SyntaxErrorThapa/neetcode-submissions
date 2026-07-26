class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        count = [[] for i in range(len(nums) + 1)]

        # Counts the frequency of digit inside nums
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        # Add frequency to it's corresponding index inside count 
        for num, freq in dic.items():
            count[freq].append(num)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res