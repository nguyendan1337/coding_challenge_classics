"""
PayPal Paired Programming Challenge

Problem:
Given a string of scrambled letters and a list of candidate words,
return all words that can be formed using the letters in the string.

Rules:
- Each letter in the scrambled string can only be used as many times as it appears.
- Matching is case-insensitive.
- Return the valid words in any order.

Example:
scrambled = "aet"
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
["eat", "tea", "ate"]

---

Approach:
- Count frequency of letters in scrambled string
- For each word, count its letters
- Check if word's letter counts are all <= scrambled counts

Time Complexity:
O(n * k) where n = number of words, k = average word length
"""

from collections import Counter
from typing import List

# chatgpt solution
# def find_valid_words(scrambled: str, words: List[str]) -> List[str]:
#     scrambled_count = Counter(scrambled.lower())
#     valid_words = []
#
#     for word in words:
#         word_count = Counter(word.lower())
#
#         # Check if word can be formed
#         can_form = True
#         for char, count in word_count.items():
#             if scrambled_count[char] < count:
#                 can_form = False
#                 break
#
#         if can_form:
#             valid_words.append(word)
#
#     return valid_words

def find_valid_words(scrambled, words):
    scrambled_count = Counter(scrambled)
    valid_words = []

    for word in words:
        word_count = Counter(word)

        success = True
        for char, count in word_count.items():
            if scrambled_count[char] < count:
                success = False
                break

        if success:
            valid_words.append(word)

    return valid_words


# ----------------------
# Test Cases
# ----------------------

def run_tests():
    tests = [
        {
            "scrambled": "bbctay",
            "words": ["cat", "baby", "dog", "mouse", "cheese", "bark"],
            "expected": ["cat", "baby"]
        },
        {
            "scrambled": "aet",
            "words": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": ["eat", "tea", "ate"]
        },
        {
            "scrambled": "listen",
            "words": ["enlist", "google", "inlets", "banana"],
            "expected": ["enlist", "inlets"]
        },
        {
            "scrambled": "aabbcc",
            "words": ["abc", "aabb", "abcc", "aabbcc", "aaa"],
            "expected": ["abc", "aabb", "abcc", "aabbcc"]
        },
        {
            "scrambled": "",
            "words": ["a", "b"],
            "expected": []
        },
        {
            "scrambled": "xyz",
            "words": [],
            "expected": []
        }
    ]

    for i, test in enumerate(tests):
        result = find_valid_words(test["scrambled"], test["words"])

        # Sort for comparison (order not guaranteed)
        result_sorted = sorted(result)
        expected_sorted = sorted(test["expected"])

        print(f"Test {i + 1}:")
        print(f"  Scrambled: {test['scrambled']}")
        print(f"  Words: {test['words']}")
        print(f"  Expected: {expected_sorted}")
        print(f"  Got: {result_sorted}")

        assert result_sorted == expected_sorted, f"Test {i + 1} failed"
        print("  Passed!\n")


if __name__ == "__main__":
    run_tests()
