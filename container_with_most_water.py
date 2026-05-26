class Solution:
    #my messy solution with bad runtime and bad space usage
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            print(f"{left} {right}")
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            elif height[left] == height[right]:
                if right == left+1:
                    break
                if height[left+1] < height[right-1]:
                    right -= 1
                elif height[left+1] >= height[right-1]:
                    left += 1

        return max_water

    def grok(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Calculate current area
            current_area = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, current_area)

            # Move the pointer with the smaller height
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_water