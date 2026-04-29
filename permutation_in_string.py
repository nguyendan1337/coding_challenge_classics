from collections import Counter
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        n = len(s1)
        for i in range(len(s2)-n+1):
            if s1_counts == Counter(s2[i:i+n]):
                return True
        return False

from collections import Counter
from typing import List

class SolutionGROK:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter()
        n = len(s1)

        # Initialize first window
        for i in range(n):
            window_count[s2[i]] += 1

        if window_count == s1_count:
            return True

        # Slide the window
        for i in range(n, len(s2)):
            # Add new character
            window_count[s2[i]] += 1
            # Remove old character
            window_count[s2[i - n]] -= 1
            if window_count[s2[i - n]] == 0:
                del window_count[s2[i - n]]   # clean up zero counts

            if window_count == s1_count:
                return True

        return False