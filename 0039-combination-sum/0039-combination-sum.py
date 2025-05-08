'''
2                 running_count     logic
2+2+2             6                 keep iterating 
2+2+2+2           8 


running_count

'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(start, path, total):
            if total == target:
                result.append(path[:])
                return 
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])
                path.pop()
        dfs(0, [], 0)
        return result