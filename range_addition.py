# brute force takes too long
# use difference array + prefix sums

def range_addition(length, updates):
    arr = [0] * length

    for start, end, inc in updates:
        arr[start] += inc
        if end + 1 < length:
            arr[end + 1] -= inc

    # Apply prefix sum to get the final values
    for i in range(1, length):
        arr[i] += arr[i - 1]

    return arr

length = 5
updates = [
    [1, 3, 2],  # add 2 to indices 1,2,3
    [2, 4, 3],  # add 3 to indices 2,3,4
    [0, 2, -2]  # subtract 2 from indices 0,1,2
]
#  [ 0,  2,  2,  2,  0]
#  [ 0,  0,  3,  3,  3]
#  [-2, -2, -2,  0,  0]
#=>[-2,  0,  3,  5,  3]

# difference array
# [ 0, 2, 0, 0, -2]
# [ 0, 2, 3, 0, -2]
# [-2, 2, 3, 2, -2]
# prefixSum
# [-2, 0, 3, 5, 3]

result = range_addition(length, updates)
print(result)