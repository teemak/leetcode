class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = defaultdict(int)
        max_score = result_node = -1

        for i, dest in enumerate(edges):
            score[dest] += i

        for node in score:
            valid = score[node] == max_score and node < result_node
            if score[node] > max_score or valid:
                max_score = score[node]
                result_node = node
        
        return result_node
