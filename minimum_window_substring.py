
#my solution which passes all but takes a while and uses a lot of memory

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) > n:
            return ""
        t_count = Counter(t)
        minimum_substring = ""

        sliding_window = []
        sliding_window_count = Counter()
        for right in range(n):

            sliding_window.append(s[right])
            sliding_window_count[s[right]] += 1

            hypothetical = sliding_window_count.copy()
            hypothetical[sliding_window[0]] -= 1

            while hypothetical >= t_count:
                c = sliding_window.pop(0)
                sliding_window_count[c] -= 1

                hypothetical = sliding_window_count.copy()
                hypothetical[sliding_window[0]] -= 1

            if (sliding_window_count >= t_count and len(sliding_window) < len(minimum_substring)) or (sliding_window_count >= t_count and minimum_substring==""):
                minimum_substring = sliding_window.copy()


        return "".join(minimum_substring)


#chatgpt solution
def chatGPT_solution(self, s: str, t: str) -> str:
    need = Counter(t)
    window = {}

    have = 0
    need_count = len(need)

    res = [-1, -1]
    res_len = float("inf")

    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        # shrink when valid
        while have == need_count:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            left_char = s[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                have -= 1

            left += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""
