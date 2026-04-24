from collections import Counter
#given string s and p, return a list of all the indices in s where the following substring is an anagram of p
def findAnagrams(s, p):
    start_indices = []
    n = len(p)
    p_counter = Counter(p)

    for i in range(len(s)):
        word_counter = Counter(s[i:i+n])
        if word_counter == p_counter:
            start_indices.append(i)

    return start_indices

s = "cbapqoweirubachjka"
p = "abc"
print(findAnagrams(s, p))