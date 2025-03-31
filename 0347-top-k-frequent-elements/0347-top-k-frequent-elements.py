import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        top_k = heapq.nlargest(k, hash_map, key=hash_map.get)

        return list(top_k)        
        