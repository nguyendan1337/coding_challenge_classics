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

def chatGPT_solution(events, k):
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
    print(elements)

#if there is a tie in occurrences, the one that appeared first wins
events = [4, 1, 2, 2, 4, 3, 1, 4]
k = 3
# print(getTopKFrequentEvents(events, k))
chatGPT_solution(events, k)