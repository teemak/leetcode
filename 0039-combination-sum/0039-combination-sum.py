class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start, path, total):
            if target == total:
                result.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)
                dfs(i, path, total + num)
                path.pop()
            
        dfs(0, [], 0)
        return result