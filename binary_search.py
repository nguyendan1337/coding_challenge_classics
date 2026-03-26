def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        if nums[mid] > target:
            high = mid - 1

    return -1

nums = [1, 3, 5, 7, 9, 11]
target = 7
print(binary_search(nums, target))