from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numFreq = defaultdict(int)
        for i in nums:
            numFreq[i] += 1
        
        minHeap = []
        for key, v in numFreq.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (v, key))
            else:
                heapq.heappush(minHeap, (v, key))
                heapq.heappop(minHeap)
        # heapq.heappop(minHeap)
        
        ans = []
        while (len(minHeap)):
            ans.append(heapq.heappop(minHeap)[1])
        return ans[::-1]