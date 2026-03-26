def longestNonRepeatingSubstring(s):
    left = 0
    longest_substring = []
    longest_substring_length = 0
    sliding_window = []

    for right in range(len(s)):
        while s[right] in sliding_window: #the sliding window contains a repeating character which makes the window invalid
            sliding_window.pop(0)
            # print(sliding_window)
            left += 1

        sliding_window.append(s[right])
        # print(sliding_window)
        # print(len(sliding_window))
        if len(sliding_window) > longest_substring_length:
            longest_substring_length = len(sliding_window)
            longest_substring = sliding_window.copy()

    return longest_substring, longest_substring_length

s = "abcabcbb"
print(longestNonRepeatingSubstring(s))

