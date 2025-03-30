class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        mapping = defaultdict(list)
        for i, c in enumerate(source):
            mapping[c].append(i)

        i = 0
        result = 1
        for c in target:
            if c not in mapping:
                return -1
            index = bisect.bisect_left(mapping[c], i)
            if index == len(mapping[c]):
                result += 1
                i = mapping[c][0] + 1
            else:
                i = mapping[c][index] + 1
        return result