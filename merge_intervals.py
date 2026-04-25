class Solution:
    #mine
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        merged = []
        previous_start = None
        previous_end = None
        for start, end in intervals:
            if previous_start is None and previous_end is None:
                previous_start = start
                previous_end = end
            elif start <= previous_end and end > previous_end:
                previous_end = end
            elif start > previous_end:
                merged.append([previous_start, previous_end])
                previous_start = start
                previous_end = end
        merged.append([previous_start, previous_end])
        return merged

    #theirs
    def chatGPT(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged