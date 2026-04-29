class NumArray:
    # sum(i,j) = prefix[j] - prefix[i-1]
    # sum(i+1,j) = prefix[j] - prefix[i]
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]*len(nums)
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            self.prefix[i] = prefix_sum


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]