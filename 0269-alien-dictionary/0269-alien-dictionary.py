class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        for first, second in zip(words, words[1:]):
            for x, y in zip(first, second):
                if x != y:
                    if y not in adj_list[x]:
                        adj_list[x].add(y)
                        indegree[y] += 1
                    break
            else:
                if len(second) < len(first):
                    return ''
        top_order = []
        queue = deque([c for c in indegree if indegree[c] == 0])

        while queue:
            char = queue.popleft()
            top_order.append(char)

            for next_char in adj_list[char]:
                indegree[next_char] -= 1
                if indegree[next_char] == 0:
                    queue.append(next_char)

        if len(top_order) != len(indegree):
            return ''
        
        return ''.join(top_order)