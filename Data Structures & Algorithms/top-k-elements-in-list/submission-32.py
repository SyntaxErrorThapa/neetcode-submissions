class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Stored in heap 
        # Adding inside heap is O(logn)
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)
        
        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]