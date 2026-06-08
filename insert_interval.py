class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = intervals.copy()
        new_intervals.append(newInterval)
        new_intervals.sort()

        result = [new_intervals[0]]

        for start, end in new_intervals[1:]:
            previous_end = result[-1][1]
            if start <= previous_end and end > previous_end:
                result[-1][1] = end
            elif start > previous_end:
                result.append([start,end])

        return result

