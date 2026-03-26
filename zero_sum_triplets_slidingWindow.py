
def chatGPT_solution(readings, windowSize):
    n = len(readings)
    if n < 3:
        return []

    result = []

    for k in range(2,n):
        start = max(0, k - windowSize + 1)
        for i in range(start, k):
            for j in range(i+1, k):
                # print(f"{i} {j} {k}")
                if readings[i] + readings[j] + readings[k] == 0:
                    result.append([readings[i], readings[j], readings[k]])

    return result


#my messy solution that only passes 2/16
def findZeroSumTripletsInWindow(readings, windowSize):
    # Write your code here
    print(readings)
    print(windowSize)
    if len(readings) < 3:
        return []
    i = 0
    j = 1
    k = 2
    result_arrays = []
    while k < len(readings):
        j = i+1
        while j < k:
            print(f"{i} {j} {k}")
            if readings[i]+readings[j]+readings[k] == 0:
                result_arrays.append([readings[i], readings[j], readings[k]])
            j += 1
        while k-i+1 >= windowSize:
            i+=1
            j = i+1
            while j < k:
                print(f"{i} {j} {k}")
                if readings[i]+readings[j]+readings[k] == 0:
                    result_arrays.append([readings[i], readings[j], readings[k]])
                j += 1
        k += 1

    return result_arrays

readings = [1, -2, 1, 0, 5]
windowSize = 3
print(findZeroSumTripletsInWindow(readings, windowSize))
print(chatGPT_solution(readings, windowSize))