from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if  endWord not in wordList:
            return 0
        elif beginWord == endWord:
            return 1

        pattern_map = defaultdict(list)
        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        queue = deque([(beginWord, 1)])
        seen = set(beginWord)

        while queue:
            word, steps = queue.popleft()
            for i in range(n):
                pattern = word[:i] + "*" + word[i+1:]
                for candidate in pattern_map[pattern]:
                    if candidate==endWord:
                        return steps+1
                    if candidate not in seen:
                        seen.add(candidate)
                        queue.append((candidate, steps+1))
                pattern_map[pattern] = [] #optimization but not necessary, seen already prevents cycles but why check against seen when you can skip

        return 0