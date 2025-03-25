class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp, username, website))
        history = {}

        for _, user, site in data:
            if user not in history:
                history[user] = []        
            history[user].append(site)

        counts = {}

        for user, sites in history.items():
            patterns = set()
            n = len(sites)

            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        pattern = (sites[i], sites[j], sites[k])
                        patterns.add(pattern)

            for pattern in patterns:
                if pattern not in counts:
                    counts[pattern] = 0
                counts[pattern] += 1

        freq = max(counts.values())
        best = min(pattern for pattern, count in counts.items() if count == freq)

        return list(best) 