def max_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    print(intervals)
    count = 0
    previous_end = -999999
    choices = []
    for start, end in intervals:
        if start >= previous_end: #no overlap, depending on the question can be > or >=
            count += 1
            previous_end = end #update previous end to current interval end
            choices.append([start, end])
    return count, choices

intervals = [[1,3], [2,5], [3,7], [4,6], [3,5], [6,7], [5,8], [5,7]]
print(max_non_overlapping_intervals(intervals))