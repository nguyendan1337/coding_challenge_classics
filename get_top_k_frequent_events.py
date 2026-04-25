import heapq
from collections import OrderedDict
from collections import Counter

#my messy solution
def getTopKFrequentEvents(events, k):
    # Write your code here
    # print(events)
    # print(k)

    if len(events) < 1:
        return []

    counts = {}

    for i in range(len(events)):
        counts.update({events[i] : counts.get(events[i], 0) + 1})
    # print(counts)
    res = OrderedDict(sorted(counts.items(), key=lambda item:item[1], reverse=True))
    # print(res)
    arr = []
    i = 0
    for key,value in res.items():
        # print(i)
        arr.append(key)
        i+=1
        if i >= k:
            break
    # print(arr)
    return arr

#llm solution that returns top k elements with tie breaker by first appearance but is not optimal
def sortCounter(events, k):
    freq = Counter(events)
    print(freq)
    first_index = {}
    for i, v in enumerate(events):
        print(f"{i} {v}")
        if v not in first_index:
            first_index[v] = i

    # so it iterates through elements grabbing an element as x
    # puts it into the lambda function -freq[x]
    # and the output of the lambda function is used to determine the placement of x in the final elements
    # output of first_index[x] is used to break the tie
    elements = list(freq.keys())
    elements.sort(key=lambda x: (-freq[x], first_index[x]))
    result = []
    for i in range(k): result.append(elements[i])
    return result

#optimal solution but returns without order or tie breaker
def optimalHeapSolution(events, k):
    freq = Counter(events)

    first_occurrence = {}
    for i, value in enumerate(events):
        if value not in first_occurrence:
            first_occurrence[value] = i

    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)



    return [num for _, num in heap]

#one-liner using Counter but not most optimal (O(nlogn) which is > O(nlogk))
def topKFrequent(nums, k):
    return [num for num, count in Counter(nums).most_common(k)]

#if there is a tie in occurrences, the one that appeared first wins
events = [4, 1, 2, 2, 4, 3, 1, 4]
k = 3
# print(getTopKFrequentEvents(events, k))
print(sortCounter(events, k))
print(optimalHeapSolution(events, k))
print(topKFrequent(events, k))