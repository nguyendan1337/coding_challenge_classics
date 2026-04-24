from typing import List

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Stack will store [char, count] pairs
        stack: List[List] = []

        for char in s:
            if stack and stack[-1][0] == char:
                # Same character -> increment count
                stack[-1][1] += 1

                # If count reaches k, remove the group
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Different character -> start new group
                stack.append([char, 1])

        # Build the final string from the stack
        result = []
        for char, count in stack:
            result.append(char * count)

        return ''.join(result)