
#my solution which passes 265/268 test cases
from collections import Counter

def substring_contains_t(substring, t_counter):
    substring_counter = Counter(substring)
    for char, count in t_counter.items():
        if char not in substring_counter or count > substring_counter[char]:
            return False

    return True
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""


        left = 0
        t_counter = Counter(t)
        min_substring = s
        substring = []
        found = False

        for right in range(m):
            substring.append(s[right])

            if substring_contains_t("".join(substring), t_counter):
                found = True

                can_shift_left = False
                if substring_contains_t("".join(substring[1:]), t_counter):
                    can_shift_left = True
                    while can_shift_left:
                        left += 1
                        substring.pop(0)
                        if not substring_contains_t("".join(substring[1:]), t_counter):
                            can_shift_left = False

            if found and len(substring) < len(min_substring):
                min_substring = "".join(substring)

        if found:
            return min_substring
        return ""

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
