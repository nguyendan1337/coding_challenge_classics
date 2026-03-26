import heapq

# chatgpt's intuitive version
def min_resources(start, end):
    tasks = list(sorted(zip(start, end)))
    resources = 0
    previous_ends = []

    for s, e in tasks:
        while previous_ends and previous_ends[0] <= s:
            heapq.heappop(previous_ends)

        heapq.heappush(previous_ends, e)
        resources = max(resources, len(previous_ends))

    return resources

# chatgpt's aha version
# def min_resources(start, end):
#     start.sort()
#     end.sort()
#
#     i = j = 0
#     current = 0
#     max_resources = 0
#     n = len(start)
#
#     while i < n and j < n:
#         if start[i] < end[j]:
#             current += 1
#             max_resources = max(max_resources, current)
#             i += 1
#         else:
#             current -= 1
#             j += 1
#
#     return max_resources




start = [10, 5, 1, 2]
end   = [11, 6, 4, 3]
print(min_resources(start, end))
