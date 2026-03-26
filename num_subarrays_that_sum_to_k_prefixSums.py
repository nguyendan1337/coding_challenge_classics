#important idea
# if prefix_sums[j] - prefix_sums[i] = k
# => prefix_sums[i] = prefix_sums[j] - k
def num_subarrays_that_sum_to_k(nums, k):
    prefix_sum_counts = { 0 : 1 } # prefix sum : how many times it has appeared
    running_sum = 0
    count = 0

    for num in nums:
        running_sum += num
        if running_sum - k in prefix_sum_counts: #if we see prefix_sums[i], then we know that prefix_sums[j] - k
            count += prefix_sum_counts[running_sum - k] #increment count by how many times you have already seen prefix[i]
        prefix_sum_counts[running_sum] = prefix_sum_counts.get(running_sum, 0) + 1
    return count

nums = [10, 5, 5, 10, 0]
#prefix_sums = [10, 15, 20, 30, 30]
k = 10
print(num_subarrays_that_sum_to_k(nums, k))