from collections import Counter
class Solution:
    #my nasty one
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        i = 0
        sliding_window = []
        sliding_window_counts = Counter()
        max_length = 0
        for j in range(n):
            sliding_window.append(s[j])
            sliding_window_counts[s[j]] += 1
            most_common_char = sliding_window_counts.most_common(1)[0][0]
            most_common_count = sliding_window_counts[most_common_char]

            while len(sliding_window) - most_common_count > k:
                popped_char = sliding_window.pop(0)
                sliding_window_counts[popped_char] -= 1
                most_common_char = sliding_window_counts.most_common(1)[0][0]
                most_common_count = sliding_window_counts[most_common_char]

            max_length = max(max_length, len(sliding_window))

        return max_length


    def grok(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = max_freq = max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length