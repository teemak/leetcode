class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(start, path, count):
            if count == 0:
                result.append(path[:])
                return
            if count > target:
                return
            for i in range(start, len(candidates)):
                if candidates[i] > count:
                    break
                path.append(candidates[i])
                dfs(i, path, count - candidates[i])
                path.pop()
        dfs(0, [], target)
        return result