class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        max_heap = [(-val, key) for key, val in hash_map.items()]
        heapify(max_heap)
        res =[]
        for i in range(k):
            freq, num = heappop(max_heap)
            res.append(num)
        return res

# Time Complexity: O(nlogk)
# Space Complexity: O(n)