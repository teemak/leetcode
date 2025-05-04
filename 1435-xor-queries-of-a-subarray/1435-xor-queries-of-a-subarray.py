class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix_sums = [0]
        result = []
        for i in range(n):
            prefix_sums.append(prefix_sums[i] ^ arr[i])
        for left, right in queries:
            result.append(prefix_sums[right + 1] ^ prefix_sums[left]) 
            
        return result