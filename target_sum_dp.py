def findTargetSumWays_dfs(nums, target):
    return dfs(0, 0)

def dfs(i, running_total):
    if i == len(nums):
        if running_total==target:
            return 1
        else:
            return 0
    return dfs(i+1, running_total - nums[i]) + dfs(i+1, running_total + nums[i])


def findTargetSumWays_dfs_dp(nums, target):
    dp = {} # (index, current_sum) -> ways
    return dfs_dp(0,0, dp)

def dfs_dp(i, total, dp):
    if i == len(nums):
        if total==target:
            return 1
        else:
            return 0

    if (i, total) in dp:
        return dp[(i, total)]

    add = dfs_dp(i+1, total + nums[i], dp)
    subtract = dfs_dp(i+1, total - nums[i], dp)

    dp[(i, total)] = add + subtract
    return dp[(i, total)]


nums = [1,1,1,1,1]
target = 3
# print(findTargetSumWays_dfs(nums, target))
print(findTargetSumWays_dfs_dp(nums, target))