
def longest_increasing_subsequence(nums):
    dp = [1]*len(nums)
    print(dp)

    for i in range(len(nums)):
        print("i:" + str(i) + "   nums[" + str(i) + "]:" + str(nums[i]))
        for j in range(i):
            print("  j:" + str(j) + " nums[" + str(j) + "]:" + str(nums[j]))
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                print(dp)

    return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums))
