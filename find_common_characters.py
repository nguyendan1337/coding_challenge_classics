class Solution:
    from collections import Counter
    def commonChars(self, words: List[str]) -> List[str]:
        seen_letters = Counter("")
        word_counters = []
        for word in words:
            word_counter = Counter(word)
            word_counters.append(word_counter)
            seen_letters += word_counter

        letter_counts = {}
        for char, count in seen_letters.items():

            found = True
            min_count = 100
            for word_counter in word_counters:
                if char not in word_counter:
                    found = False
                    break
                min_count = min(min_count, word_counter[char])
            if found:
                letter_counts[char] = min_count

        result = []
        for char, count in letter_counts.items():
            result += [char]*count

        return result


from typing import List

class SolutionGROK:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # Start with the frequency of the first word
        common = Counter(words[0])

        # For every subsequent word, keep only the min count for each char
        for word in words[1:]:
            current = Counter(word)
            for char in list(common.keys()):   # list() to avoid runtime modification issues
                if char in current:
                    common[char] = min(common[char], current[char])
                else:
                    del common[char]   # or common[char] = 0

        # Build the result
        result = []
        for char, count in common.items():
            result.extend([char] * count)

        return result