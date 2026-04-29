"""
🔹 Meeting Rooms II
🔗 https://leetcode.com/problems/meeting-rooms-ii/

Problem:
Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
return the minimum number of conference rooms required.

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= start_i < end_i <= 10^6

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Explanation:
We need to allocate rooms such that no meetings that overlap are in the same room.

Key Idea:
- If a meeting starts before another ends → need a new room
- Otherwise, reuse a room

Optimal Approach:
- Sort meetings by start time
- Use a min-heap (priority queue) to track earliest ending meeting
- If current meeting starts after the earliest end → reuse room
- Else → allocate new room

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List
import heapq


def minMeetingRooms(intervals: List[List[int]]) -> int:
    """
    TODO: Implement this function.

    Args:
        intervals: List of [start, end] meeting times

    Returns:
        Minimum number of meeting rooms required
    """
    if not intervals:
        return 0
    sorted_events = []
    for start, end in intervals:
        sorted_events.append((start, 1))
        sorted_events.append((end, -1))
    sorted_events.sort()

    current_overlap = 0
    max_overlap = 0
    for event, value in sorted_events:
        current_overlap += value
        max_overlap = max(max_overlap, current_overlap)

    return max_overlap


# ------------------------
# Test Cases
# ------------------------

def run_tests():
    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [8, 9], [8, 9]], 2),
        ([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]], 4),
        ([], 0),
        ([[1, 2]], 1),
        ([[1, 5], [5, 10]], 1),  # edge: touching intervals
    ]

    for i, (intervals, expected) in enumerate(test_cases):
        result = minMeetingRooms(intervals)
        print(f"Test Case {i + 1}: ", end="")
        if result == expected:
            print("✅ Passed")
        else:
            print(f"❌ Failed (Expected {expected}, Got {result})")


if __name__ == "__main__":
    run_tests()