# Prefix Sum IDEA
# arr    = [3, 4, 2, 7]
# prefix = [3, 7, 9, 16]
# key idea: prefix[j] - prefix[i] = sum(i+1 -> j)
# key idea: sum(i+1 -> j) = prefix[j] - prefix[i]
# example sum(1+1 -> 3) = prefix[3] - prefix[1]
# =>           2  +  7  = 16        - 7 = 9

# TRICK: subarray_sum = target
# prefix[j] - prefix[i] = target
# prefix[i] = prefix[j] - target
# If we have seen a previous prefix sum equal to prefix[j] - target, then a valid subarray exists.


def countNumberOfSubarrays(arr, k):
    # Write your code here
    prefix = 0
    seen = {0: 1} #key: seen prefix sum, value: how many times that prefix sum is seen
    count = 0

    for num in arr:
        prefix += num
        if prefix - k in seen:
            count += seen[prefix - k]
        seen[prefix] = seen.get(prefix, 0) + 1
    return count

#should return 3
print(countNumberOfSubarrays([10, 2, -2, -20, 10], -10))