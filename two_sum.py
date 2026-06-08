class Solution:
    #dum edition
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return -1

    #hella optimized hashmap single pass edition
    def smart(self, nums: List[int], target: int) -> List[int]:

        seen_complements = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen_complements:
                return [seen_complements[complement], i]

            seen_complements[num] = i