from collections import Counter
class Solution:
    #my solution
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        consumed = [False]*n

        anagram_groups = []
        for i in range(n):
            added = False
            if not consumed[i]:
                word = strs[i]
                word_counter = Counter(word)
                word_group = [word]
                consumed[i] = True
                added = True

                for j in range(i+1, n):
                    if not consumed[j] and Counter(strs[j]) == word_counter:
                        word_group.append(strs[j])
                        consumed[j] = True

            if added: anagram_groups.append(word_group)

        return anagram_groups

    # chatgpt solution
    # my original solution was o use the counter as a dict key
    # if the counter has been seen before then append the word to the dictionary value which is a list of words.
    # however, counter cant be used as a dict key.
    # this chatgpt solution solves this issue by using the sorted word as the key, bruh
    from collections import Counter, defaultdict
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            groups[key].append(word)

        return list(groups.values())