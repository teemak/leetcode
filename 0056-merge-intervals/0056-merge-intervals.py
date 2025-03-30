class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0

        while i < len(intervals) - 1:
            curr_start, curr_end = intervals[i]
            next_start, next_end = intervals[i + 1]

            if curr_end >= next_start:
                intervals[i][1] = max(curr_end, next_end)
                intervals.pop(i + 1)
            else:
                i += 1

        return intervals

                

