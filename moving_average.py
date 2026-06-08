"""
LeetCode 346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last 'size' values of the stream.

Example:
MovingAverage m = new MovingAverage(3);
m.next(1) = 1.0
m.next(10) = (1 + 10) / 2 = 5.5
m.next(3) = (1 + 10 + 3) / 3 = 4.666...
m.next(5) = (10 + 3 + 5) / 3 = 6.0

Constraints:
- 1 <= size <= 1000
- -10^5 <= val <= 10^5
- At most 10^4 calls will be made to next.
"""

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        # TODO: Complete the initialization
        pass

    def next(self, val: int) -> float:
        """
        :type val: int
        :rtype: float
        """
        # TODO: Implement the next method to return the moving average
        pass


# ==================== TEST CASES ====================

if __name__ == "__main__":
    print("Running test cases for LeetCode 346 - Moving Average from Data Stream\n")

    # Test Case 1
    ma = MovingAverage(3)
    print("next(1)  ->", ma.next(1))   # Expected: 1.0
    print("next(10) ->", ma.next(10))  # Expected: 5.5
    print("next(3)  ->", ma.next(3))   # Expected: 4.666...
    print("next(5)  ->", ma.next(5))   # Expected: 6.0

    # Test Case 2: Smaller window
    ma2 = MovingAverage(1)
    print("\nTest Case 2 (size=1):")
    print("next(5)  ->", ma2.next(5))   # Expected: 5.0
    print("next(10) ->", ma2.next(10))  # Expected: 10.0
    print("next(-3) ->", ma2.next(-3))  # Expected: -3.0

    # Test Case 3: Larger window
    ma3 = MovingAverage(4)
    print("\nTest Case 3 (size=4):")
    print("next(1)  ->", ma3.next(1))   # 1.0
    print("next(2)  ->", ma3.next(2))   # 1.5
    print("next(3)  ->", ma3.next(3))   # 2.0
    print("next(4)  ->", ma3.next(4))   # 2.5
    print("next(5)  ->", ma3.next(5))   # 3.5 (2+3+4+5)/4

    print("\nAll test cases completed. Implement the class above to pass them!")