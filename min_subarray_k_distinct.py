from collections import Counter

#mine
def findMinimumLengthSubarray(arr, k):
    # Write your code here

    min_length = 9999999
    sliding_window = []
    found = False
    count = Counter()
    for j in range(len(arr)):
        sliding_window.append(arr[j])
        count[arr[j]] += 1
        while len(count) >= k:
            found = True
            min_length = min(min_length, len(sliding_window))
            pop = sliding_window[0]
            count[pop] -= 1
            if count[pop] <= 0:
                del count[pop]
            if len(count) < k:
                count[pop] += 1
                break
            else:
                sliding_window.pop(0)

    if found:
        return min_length
    else:
        return -1

#chatGPT's
from collections import Counter


def findMinimumLengthSubarray(arr, k):
    count = Counter()
    left = 0
    min_length = float("inf")

    for right in range(len(arr)):
        count[arr[right]] += 1

        while len(count) >= k:
            min_length = min(min_length, right - left + 1)

            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                del count[arr[left]]

            left += 1

    return min_length if min_length != float("inf") else -1