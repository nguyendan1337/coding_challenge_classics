def elements_that_sum_to_target(nums, target):
    left = 0
    right = len(nums)-1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return True, [nums[left], nums[right]]
        if sum < target: # need bigger sum
            left += 1
        if sum > target: # need smaller sum
            right -= 1

    return False, []

nums = [1, 2, 6, 7, 9]
target = 13
print(elements_that_sum_to_target(nums, target))
