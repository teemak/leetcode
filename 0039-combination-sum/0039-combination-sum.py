class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start, path, running_count):
            if running_count == target:
                result.append(path[:])
                return
            if running_count > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, running_count + candidates[i])
                path.pop()
        dfs(0, [], 0)
        return result