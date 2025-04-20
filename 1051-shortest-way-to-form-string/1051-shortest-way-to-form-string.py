class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        char_idx = defaultdict(list)

        for i, c in enumerate(source):
            char_idx[c].append(i)

        count, i, pos = 1, 0, -1

        while i < len(target):
            c = target[i]
            if c not in char_idx:
                return -1

            idx_list = char_idx[c]
            j = bisect.bisect_right(idx_list, pos)
            
            if j == len(idx_list):
                count += 1
                pos = -1
            else:
                pos = idx_list[j]
                i += 1

        return count
